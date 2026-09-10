// Приём заявок с формы и отправка их в Telegram.
// Токен бота живёт в переменных окружения Vercel и в браузер не попадает.
// Настройка описана в README.md.

const LIMITS = { name: 80, contact: 120, level: 60, goal: 60, device: 60 };

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

  const lead = {
    name: clean(body.name, LIMITS.name),
    contact: clean(body.contact, LIMITS.contact),
    level: clean(body.level, LIMITS.level),
    goal: clean(body.goal, LIMITS.goal),
    device: clean(body.device, LIMITS.device),
  };

  if (!lead.name || !lead.contact) {
    return res.status(400).json({ ok: false, error: 'missing_fields' });
  }

  const text =
    '<b>Новая заявка — gen z vibecoding</b>\n\n' +
    `<b>Имя:</b> ${esc(lead.name)}\n` +
    `<b>Контакт:</b> ${esc(lead.contact)}\n` +
    `<b>Уровень:</b> ${esc(lead.level || '—')}\n` +
    `<b>Цель:</b> ${esc(lead.goal || '—')}\n` +
    `<b>Устройство:</b> ${esc(lead.device || '—')}`;

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
    });

    if (!tg.ok) {
      // отдаём причину наружу: в ней нет токена, зато без неё непонятно,
      // что чинить — токен, chat_id или не нажатый Start у бота
      const info = await tg.json().catch(() => ({}));
      const description = info.description || 'нет описания';
      console.error('Telegram ответил ошибкой:', tg.status, description);
      return res.status(502).json({
        ok: false,
        error: 'telegram_failed',
        tg_status: tg.status,
        tg_description: description,
      });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Не удалось достучаться до Telegram:', err);
    return res.status(502).json({ ok: false, error: 'telegram_unreachable' });
  }
};
