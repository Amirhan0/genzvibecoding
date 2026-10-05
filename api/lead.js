// Приём заявок с формы и отправка их в Telegram.
// Токен бота живёт в переменных окружения Vercel и в браузер не попадает.
// Настройка описана в README.md.

const LIMITS = { direction: 40, name: 80, contact: 120, level: 60, goal: 200, device: 60, card: 40, source: 100 };

const clean = (v, max) =>
  String(v ?? '').replace(/\s+/g, ' ').trim().slice(0, max);

// экранируем под parse_mode: 'HTML', иначе имя вида "<Амир>" сломает сообщение
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  }

  // .trim() — потому что при копировании в панель Vercel легко утащить пробел
  // или перевод строки, и тогда Telegram молча отвечает 401.
  // Заодно срезаем префикс "bot", если токен скопировали вместе с ним.
  const token = String(process.env.TELEGRAM_BOT_TOKEN || '').trim().replace(/^bot/, '');
  const chatId = String(process.env.TELEGRAM_CHAT_ID || '').trim();
  if (!token || !chatId) {
    console.error('Не заданы TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID');
    return res.status(500).json({ ok: false, error: 'not_configured' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch { body = null; }
  }
  if (!body || typeof body !== 'object') {
    return res.status(400).json({ ok: false, error: 'bad_request' });
  }

  // ловушка для ботов: поле скрыто от людей, заполнить его мог только робот.
  // отвечаем успехом, чтобы спамер не понял, что его отсекли.
  if (clean(body.company, 50)) return res.status(200).json({ ok: true });

  // вторая ловушка: t — сколько миллисекунд прошло от загрузки страницы до отправки.
  // человек не заполнит форму быстрее трёх секунд, бот — запросто. тоже отвечаем успехом.
  const t = Number(body.t);
  if (Number.isFinite(t) && t > 0 && t < 3000) return res.status(200).json({ ok: true });

  const lead = {
    direction: clean(body.direction, LIMITS.direction),
    name: clean(body.name, LIMITS.name),
    contact: clean(body.contact, LIMITS.contact),
    level: clean(body.level, LIMITS.level),
    goal: clean(body.goal, LIMITS.goal),
    device: clean(body.device, LIMITS.device),
    card: clean(body.card, LIMITS.card),
    source: clean(body.source, LIMITS.source), // location.search: ?utm_source=... и т. п.
  };

  if (!lead.name || !lead.contact) {
    return res.status(400).json({ ok: false, error: 'missing_fields' });
  }

  // форма курса и форма предзаписи на главной шлют разный набор полей,
  // поэтому необязательные строки показываем, только если они заполнены
  const rows = [
    ['Направление', lead.direction],
    ['Имя', lead.name],
    ['Контакт', lead.contact],
    ['Уровень', lead.level],
    ['Цель', lead.goal],
    ['Устройство', lead.device],
    ['Подписка Claude', lead.card],
    ['Источник', lead.source],
  ].filter(([, v]) => v);

  const text =
    '<b>Новая заявка · gen z school</b>\n\n' +
    rows.map(([k, v]) => `<b>${k}:</b> ${esc(v)}`).join('\n');

  try {
    const tg = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: chatId,
        text,
        parse_mode: 'HTML',
        disable_web_page_preview: true,
      }),
      // не держим функцию до таймаута Vercel, если Telegram завис
      signal: AbortSignal.timeout(8000),
    });

    if (!tg.ok) {
      // причину пишем только в логи Vercel (Deployments → Functions → Logs):
      // по ней видно, что чинить — токен, chat_id или не нажатый Start у бота.
      // наружу её не отдаём.
      const info = await tg.json().catch(() => ({}));
      const description = info.description || 'нет описания';
      console.error('Telegram ответил ошибкой:', tg.status, description);
      return res.status(502).json({ ok: false, error: 'telegram_failed' });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Не удалось достучаться до Telegram:', err);
    return res.status(502).json({ ok: false, error: 'telegram_unreachable' });
  }
};
