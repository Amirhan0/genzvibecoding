"""Второй поток: сторис 1080x1920 (s-*) и карусель для ленты 1080x1350 (p-*): python3 build.py"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
SITE = HERE.parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T, P = "#81DAD3", "#FF2E9F"
LOGO = f'<svg viewBox="0 0 120 120"><path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" fill="{T}"/><rect x="33" y="42" width="11" height="24" rx="5.5" fill="#000"/><rect x="76" y="40" width="11" height="24" rx="5.5" fill="#000"/><path d="M34 78 Q60 104 86 76" fill="none" stroke="#000" stroke-width="11" stroke-linecap="round"/></svg>'
SPARK = f'<svg viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{P}"/></svg>'
CHECK = '<svg viewBox="0 0 24 24"><path d="M4.8 12.6 9.6 17.4 19.2 6.9" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

WORKS = [  # работы учеников первого потока: скриншот, подпись
    ("got-shop", "Чайная лавка", "Gardens of Tavria"),
    ("denis-shutov", "Психолог", "Денис Шутов"),
    ("goats-running", "Беговой клуб", "Адиль · GOATS"),
]

def css(h):
    return f"""*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:{h}px;background:#000;overflow:hidden}}
body{{position:relative;font-family:Montserrat,sans-serif;color:#fff}}
.a{{position:absolute}}
.g1{{width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,rgba(129,218,211,.18),transparent 62%)}}
.g2{{width:950px;height:950px;border-radius:50%;background:radial-gradient(circle,rgba(255,46,159,.17),transparent 62%)}}
.brand{{left:72px;top:70px;display:flex;align-items:center;gap:18px;font-size:36px;font-weight:800}}
.brand svg{{width:60px;height:60px}} .brand b{{color:{T}}}
.cnt{{right:72px;top:84px;font-size:30px;font-weight:700;color:#77777f}} .cnt b{{color:#fff}}
.k{{left:76px;font-size:27px;letter-spacing:8px;color:{T};font-weight:700}}
.h{{left:68px;right:68px;font-weight:900;letter-spacing:-5px;line-height:.98}}
.h span{{color:{T}}} .h i{{font-style:normal;color:{P}}}
.t{{left:76px;right:76px;font-size:38px;line-height:1.4;color:#cfcfd8;font-weight:500}}
.t b{{color:#fff;font-weight:700}}
.box{{left:68px;right:68px;border-radius:40px;background:#0f0f12;box-shadow:inset 0 0 0 2px #24242a;padding:36px 46px}}
.row{{display:flex;gap:26px;align-items:center;padding:22px 0;border-bottom:2px solid #1e1e24}}
.row:last-child{{border:0}}
.row .n{{flex:none;font:900 50px/1 Montserrat;color:{P};width:76px}}
.row i.c{{flex:none;width:56px;height:56px;border-radius:50%;background:{T};display:grid;place-items:center}}
.row i.c svg{{width:32px;height:32px}}
.row h3{{font-size:40px;font-weight:800;line-height:1.15;letter-spacing:-1px}}
.row p{{font-size:30px;color:#a6a6b2;line-height:1.3;font-weight:500;margin-top:4px}}
.was{{font-size:28px;color:#6f6f7a;text-decoration:line-through;font-weight:600;margin-bottom:4px}}
.facts{{left:68px;right:68px;display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.fact{{border-radius:34px;background:#0f0f12;box-shadow:inset 0 0 0 2px #24242a;padding:30px 36px}}
.fact b{{display:block;font-size:76px;font-weight:900;letter-spacing:-3px;line-height:1}}
.fact span{{display:block;font-size:30px;color:#a6a6b2;font-weight:600;margin-top:10px}}
.fact.acc{{background:{T};color:#000;box-shadow:none}} .fact.acc span{{color:#000;opacity:.7}}
.phones{{left:40px;right:40px;display:flex;justify-content:center;gap:30px}}
.ph{{text-align:center}}
.ph .f{{width:290px;border-radius:40px;border:9px solid #1d1d22;overflow:hidden;background:#111;box-shadow:0 30px 70px -20px rgba(129,218,211,.35)}}
.ph .f img{{display:block;width:100%}}
.ph .k2{{margin-top:22px;font-size:24px;letter-spacing:4px;color:{T};font-weight:700;text-transform:uppercase}}
.ph .nm{{font-size:32px;font-weight:800;margin-top:6px}}
.cta{{left:68px;right:68px;border-radius:40px;background:{T};color:#000;padding:36px 48px}}
.pink{{color:{P};font-weight:900;font-style:italic;letter-spacing:-1px}}
.tag{{left:0;right:0;bottom:66px;text-align:center;font-size:26px;letter-spacing:10px;color:#9a9aa6}}
.foot{{left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;font-size:24px;color:#77777f;font-weight:600}}
.foot b{{color:{T}}}
"""

def page(inner, n, total, h, glow, swipe=False):
    if h == 1920:
        bottom = '<div class="a tag">no thoughts, just ship it</div>'
    else:
        r = '<span>листайте <b>→</b></span>' if swipe and n < total else '<span>@genz.school.kz</span>'
        bottom = f'<div class="a foot"><span>no thoughts, just ship it</span>{r}</div>'
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>{css(h)}</style></head><body>
<div class="a g1" style="right:{glow[0]};top:{glow[1]}"></div>
<div class="a g2" style="left:{glow[2]};top:{glow[3]}"></div>
<div class="a brand">{LOGO}<span>gen z <b>school</b></span></div>
<div class="a cnt"><b>{n}</b> / {total}</div>
{inner}
{bottom}
</body></html>'''

def phones(top, scale=1.0):
    items = ''.join(
        f'<div class="ph"><div class="f"><img src="{(SITE / "works" / slug / "shot.png").as_uri()}"></div>'
        f'<div class="k2">{kind}</div><div class="nm">{name}</div></div>'
        for slug, kind, name in WORKS)
    return f'<div class="a phones" style="top:{top}px;transform:scale({scale});transform-origin:top center">{items}</div>'

def rows(items, numbered=True):
    out = ''
    for i, (title, text) in enumerate(items, 1):
        mark = f'<span class="n">{i:02d}</span>' if numbered else f'<i class="c">{CHECK}</i>'
        out += f'<div class="row">{mark}<div><h3>{title}</h3>{f"<p>{text}</p>" if text else ""}</div></div>'
    return out

OUT = {}

# ================= СТОРИС =================
S = 4
OUT["s-1"] = (1920, page(f'''
<div class="a k" style="top:290px">НАБОР ОТКРЫТ</div>
<div class="a h" style="top:350px;font-size:150px">Второй<br>поток<br><span>14 ноября</span></div>
<div class="a" style="right:80px;top:470px;width:210px;height:210px;transform:rotate(10deg)">{LOGO}<div style="position:absolute;width:66px;height:66px;top:-10px;right:-12px">{SPARK}</div></div>
<div class="a facts" style="top:930px">
  <div class="fact"><b>2</b><span>недели</span></div>
  <div class="fact"><b>5+1</b><span>эфиров + демо-день</span></div>
  <div class="fact"><b>15</b><span>мест в группе</span></div>
  <div class="fact acc"><b>40К ₸</b><span>за весь курс</span></div>
</div>
<div class="a t" style="top:1400px">Курс вайбкодинга: <b>свой сайт с нуля за две недели</b>, без знания кода. ИИ пишет код — ты объясняешь задачу словами.</div>
<div class="a pink" style="left:76px;top:1660px;font-size:44px;transform:rotate(-3deg)">первый поток уже сделал свои сайты ✦</div>
''', 1, S, 1920, ("-300px", "150px", "-320px", "1150px")))

OUT["s-2"] = (1920, page(f'''
<div class="a k" style="top:290px">ЧТО НОВОГО</div>
<div class="a h" style="top:350px;font-size:118px">Программа<br><span>стала мощнее</span></div>
<div class="a box" style="top:640px;padding:22px 46px">
  <div class="row"><i class="c">{CHECK}</i><div><div class="was">сайт в сети на 3-м уроке</div><h3>Сайт в интернете в первый же вечер</h3></div></div>
  <div class="row"><i class="c">{CHECK}</i><div><div class="was">только форма в Telegram</div><h3>Заявки в Telegram + база данных</h3></div></div>
  <div class="row"><i class="c">{CHECK}</i><div><div class="was">домен «как-нибудь потом»</div><h3>Свой домен, Google и аналитика</h3></div></div>
  <div class="row"><i class="c">{CHECK}</i><div><div class="was" style="text-decoration:none;color:{P};font-weight:800;letter-spacing:3px">НОВОЕ</div><h3>Как найти первого заказчика</h3></div></div>
  <div class="row"><i class="c">{CHECK}</i><div><div class="was">разбор работ</div><h3>Демо-день и сертификат</h3></div></div>
</div>
''', 2, S, 1920, ("-260px", "900px", "-320px", "200px")))

OUT["s-3"] = (1920, page(f'''
<div class="a k" style="top:290px">РЕЗУЛЬТАТ ПЕРВОГО ПОТОКА</div>
<div class="a h" style="top:350px;font-size:118px">Это сделали<br><span>ученики</span></div>
{phones(700)}
<div class="a t" style="top:1520px;text-align:center">За две недели, <b>без опыта в коде</b>.<br>Сайты уже работают — открой любой.</div>
''', 3, S, 1920, ("-300px", "500px", "-320px", "1200px")))

OUT["s-4"] = (1920, page(f'''
<div class="a k" style="top:290px">ЗА 40 000 ₸ ТЫ ПОЛУЧАЕШЬ</div>
<div class="a h" style="top:350px;font-size:118px">Не курс,<br>а <span>готовый сайт</span></div>
<div class="a box" style="top:650px;padding:22px 46px">
  {rows([("5 живых эфиров и демо-день", ""), ("Сайт с заявками, базой и доменом", ""), ("Проверку каждой домашки", "лично, а не ботом"), ("Записи всех уроков", "")], numbered=False)}
</div>
<div class="a cta" style="top:1360px">
  <div style="font-size:30px;font-weight:700;opacity:.7">🎁 Пришёл по приглашению друга?</div>
  <div style="font-size:52px;font-weight:900;letter-spacing:-1px;margin-top:6px">35 000 ₸</div>
  <div style="font-size:34px;font-weight:800;margin-top:14px">Заявка: genzschool.vercel.app</div>
</div>
''', 4, S, 1920, ("-260px", "200px", "-320px", "1150px")))

# ================= КАРУСЕЛЬ =================
N = 6
OUT["p-1"] = (1350, page(f'''
<div class="a k" style="top:240px">ВТОРОЙ ПОТОК · 14 НОЯБРЯ</div>
<div class="a h" style="top:290px;font-size:132px">Сайт без<br>кода за<br><span>2 недели</span></div>
<div class="a t" style="top:810px;right:420px">Обновили программу после первого потока. <b>Рассказываем, что стало лучше.</b></div>
<div class="a" style="right:90px;top:800px;width:280px;height:280px;transform:rotate(-8deg)">{LOGO}<div style="position:absolute;width:86px;height:86px;top:-14px;right:-18px">{SPARK}</div></div>
''', 1, N, 1350, ("-260px", "80px", "-300px", "760px"), True))

OUT["p-2"] = (1350, page(f'''
<div class="a k" style="top:240px">К ДЕМО-ДНЮ У ТЕБЯ БУДЕТ</div>
<div class="a h" style="top:290px;font-size:104px">Не макет,<br>а <span>рабочий сайт</span></div>
<div class="a box" style="top:560px;padding:18px 46px">
  {rows([("Свой сайт в интернете", "открывается с телефона у кого угодно"), ("Заявки в Telegram и база", "ни одна заявка не потеряется"), ("Свой домен и Google", "сайт находят, а ссылка выглядит солидно"), ("Кейс для портфолио", "и план, как сделать первый сайт за деньги")], numbered=False)}
</div>
''', 2, N, 1350, ("-200px", "700px", "-300px", "60px"), True))

OUT["p-3"] = (1350, page(f'''
<div class="a k" style="top:240px">ПРОГРАММА</div>
<div class="a h" style="top:290px;font-size:104px">5 уроков<br>и <span>демо-день</span></div>
<div class="a box" style="top:560px;padding:10px 46px">
  {rows([("Первый сайт в интернете", ""), ("ИИ как профи: версии, план, баги", ""), ("Дизайн по референсам", ""), ("Заявки в Telegram и база данных", ""), ("Домен, Google, первый заказчик", ""), ("Демо-день и сертификат", "")])}
</div>
''', 3, N, 1350, ("-260px", "600px", "-300px", "100px"), True))

OUT["p-4"] = (1350, page(f'''
<div class="a k" style="top:240px">ПЕРВЫЙ ПОТОК</div>
<div class="a h" style="top:290px;font-size:104px">Сделали<br><span>ученики</span></div>
{phones(560, .86)}
''', 4, N, 1350, ("-300px", "400px", "-300px", "700px"), True))

OUT["p-5"] = (1350, page(f'''
<div class="a k" style="top:240px">ПОЧЕМУ ЭТО ВЫГОДНО</div>
<div class="a h" style="top:290px;font-size:104px">Платишь<br><span>один раз</span></div>
<div class="a box" style="top:560px;padding:18px 46px">
  {rows([("≈ 8 000 ₸ за урок", "живой эфир с разработчиком, а не запись"), ("Каждая домашка — с разбором", "проверяем лично вдвоём с Диасом"), ("Дальше делаешь сайты сам", "себе, знакомым и первым заказчикам"), ("С другом — 35 000 ₸", "а он получит 5 000 ₸ за тебя")], numbered=False)}
</div>
''', 5, N, 1350, ("-200px", "100px", "-300px", "760px"), True))

OUT["p-6"] = (1350, page(f'''
<div class="a k" style="top:240px">ЗАПИСЬ ОТКРЫТА</div>
<div class="a h" style="top:290px;font-size:132px">Старт<br><span>14 ноября</span></div>
<div class="a t" style="top:640px"><b>15 мест</b> в группе — чтобы успеть ответить каждому и проверить каждую работу.</div>
<div class="a cta" style="top:880px">
  <div style="font-size:28px;font-weight:700;opacity:.7">40 000 ₸ · с другом 35 000 ₸</div>
  <div style="font-size:48px;font-weight:900;letter-spacing:-1px;margin-top:6px">genzschool.vercel.app</div>
  <div style="font-size:32px;font-weight:800;margin-top:8px">Telegram @ameerqan · @p1kato</div>
</div>
''', 6, N, 1350, ("-260px", "80px", "-300px", "760px")))

for name, (h, html) in OUT.items():
    src = HERE / f"{name}.html"
    src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--allow-file-access-from-files", f"--window-size=1080,{h}", "--force-device-scale-factor=1",
                    "--virtual-time-budget=6000", f"--screenshot={HERE / (name + '.png')}", src.as_uri()],
                   check=True, capture_output=True)
    src.unlink()
    print("готово:", name + ".png")
