"""Карточки для «Актуального» в Instagram: python3 build.py"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TEAL, PINK = "#81DAD3", "#FF2E9F"

LOGO = f'''<svg viewBox="0 0 120 120"><path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" fill="{TEAL}"/><rect x="33" y="42" width="11" height="24" rx="5.5" fill="#000"/><rect x="76" y="40" width="11" height="24" rx="5.5" fill="#000"/><path d="M34 78 Q60 104 86 76" fill="none" stroke="#000" stroke-width="11" stroke-linecap="round"/></svg>'''
SPARK = f'<svg viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{PINK}"/></svg>'
CHECK = '<svg viewBox="0 0 24 24"><path d="M4.8 12.6 9.6 17.4 19.2 6.9" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;background:#000;overflow:hidden}}
body{{position:relative;font-family:'Montserrat',sans-serif;color:#fff}}
.abs{{position:absolute}}
.marker{{font-family:'Permanent Marker',cursive;line-height:.95;text-transform:uppercase}}
.g1{{width:950px;height:950px;border-radius:50%;background:radial-gradient(circle,rgba(129,218,211,.18),transparent 62%)}}
.g2{{width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(255,46,159,.17),transparent 62%)}}
.brand{{left:72px;top:74px;display:flex;align-items:center;gap:18px;font-size:38px;font-weight:800;letter-spacing:-1px}}
.brand svg{{width:64px;height:64px}}
.brand b{{color:{TEAL};font-weight:800}}
.count{{right:72px;top:86px;font-size:30px;font-weight:700;color:#8b8b98;letter-spacing:2px}}
.count b{{color:#fff}}
.kicker{{left:76px;font-size:28px;letter-spacing:8px;color:{TEAL};font-weight:700}}
.h{{left:68px;right:68px;font-weight:900;letter-spacing:-5px;line-height:.95}}
.h span{{color:{TEAL}}}
.lead{{left:76px;right:76px;font-size:42px;line-height:1.38;color:#d4d4dc;font-weight:500}}
.lead b{{color:#fff;font-weight:700}}
.panel{{left:68px;right:68px;border-radius:44px;background:#0f0f12;box-shadow:inset 0 0 0 2px #24242a;padding:46px 50px}}
.row{{display:flex;gap:30px;align-items:flex-start;padding:26px 0;border-bottom:2px solid #1e1e24}}
.row:last-child{{border:0}}
.row i{{flex:none;width:62px;height:62px;border-radius:50%;background:{TEAL};display:grid;place-items:center;margin-top:2px}}
.row i svg{{width:36px;height:36px}}
.row .n{{flex:none;font:900 54px/1 Montserrat;color:{PINK};width:80px}}
.row h3{{font-size:44px;font-weight:800;line-height:1.15;margin-bottom:8px;letter-spacing:-1px}}
.row p{{font-size:33px;color:#a6a6b2;line-height:1.35;font-weight:500}}
.tag{{left:0;right:0;bottom:70px;text-align:center;font-size:26px;letter-spacing:10px;color:#9a9aa6}}
.pill{{display:inline-block;background:{PINK};color:#fff;font-weight:900;font-size:28px;letter-spacing:2px;padding:14px 26px;border-radius:16px}}
"""

def page(n, total, inner, glow=("-280px","120px","-300px","1100px")):
    return f'''<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&family=Permanent+Marker&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="abs g1" style="right:{glow[0]};top:{glow[1]}"></div>
<div class="abs g2" style="left:{glow[2]};top:{glow[3]}"></div>
<div class="abs brand">{LOGO}<span>gen z <b>school</b></span></div>
{f'<div class="abs count"><b>{n}</b> / {total}</div>' if n else ''}
{inner}
<div class="abs tag">no thoughts, just ship it</div>
</body></html>'''

T = 4
CARDS = {}

# 1. кто мы
CARDS["1-kto-my"] = page(1, T, f'''
<div class="abs kicker" style="top:330px">КТО МЫ</div>
<div class="abs h" style="top:390px;font-size:150px">Учим<br>создавать<br><span>с нуля</span></div>
<svg class="abs" style="left:70px;top:822px;width:470px;height:40px" viewBox="0 0 380 40"><path d="M8 28 C110 10 260 8 372 22" stroke="{TEAL}" stroke-width="9" stroke-linecap="round" fill="none"/></svg>
<div class="abs lead" style="top:900px">IT, дизайн и другие направления. Даже если вы никогда этим не занимались: <b>объясняем простыми словами, делаем вместе на живых эфирах</b> и доводим до результата, который не стыдно показать.</div>
<div class="abs" style="left:68px;right:68px;top:1240px;display:flex;align-items:center;gap:44px">
  <div style="width:300px;height:300px;flex:none;position:relative;transform:rotate(-6deg)">{LOGO}<div style="position:absolute;width:90px;height:90px;top:-14px;right:-16px">{SPARK}</div></div>
  <div class="marker" style="font-size:52px;color:{PINK};transform:rotate(-6deg)">less theory<br>more doing</div>
</div>
''')

# 2. кто ведёт
CARDS["2-kto-vedet"] = page(2, T, f'''
<div class="abs kicker" style="top:330px">КТО ВЕДЁТ</div>
<div class="abs h" style="top:390px;font-size:104px">Ваши<br><span>преподаватели</span></div>

<div class="abs panel" style="top:690px;padding:40px 46px">
  <div style="display:flex;gap:34px;align-items:center">
    <div style="flex:none;width:150px;height:150px;border-radius:50%;background:linear-gradient(135deg,{TEAL},#3f8f88);display:grid;place-items:center;font:900 70px Montserrat;color:#000">А</div>
    <div><div style="font-size:62px;font-weight:900;letter-spacing:-2px;line-height:1">Амир</div>
      <div style="margin-top:14px"><span class="pill">РАЗРАБОТЧИК</span></div></div>
  </div>
  <p style="font-size:34px;color:#b9b9c4;line-height:1.38;margin-top:28px;font-weight:500">Каждый день пишет код и делает реальные проекты. Показывает то, чем работает сам.</p>
</div>

<div class="abs panel" style="top:1150px;padding:40px 46px">
  <div style="display:flex;gap:34px;align-items:center">
    <div style="flex:none;width:150px;height:150px;border-radius:50%;background:linear-gradient(135deg,{PINK},#a8145f);display:grid;place-items:center;font:900 70px Montserrat;color:#fff">Д</div>
    <div><div style="font-size:62px;font-weight:900;letter-spacing:-2px;line-height:1">Диас</div>
      <div style="margin-top:14px"><span class="pill" style="background:{TEAL};color:#000">ПРЕПОДАВАТЕЛЬ</span></div></div>
  </div>
  <p style="font-size:34px;color:#b9b9c4;line-height:1.38;margin-top:28px;font-weight:500">Объясняет простыми словами, отвечает на вопросы и помогает дойти до результата.</p>
</div>

<div class="abs" style="left:76px;right:76px;top:1600px;font-size:36px;font-weight:700;line-height:1.35">Каждую домашнюю работу <span style="color:{TEAL}">проверяем сами</span>. Не бот и не автопроверка.</div>
''', glow=("-300px","500px","-320px","1200px"))

# 3. чем отличаемся
CARDS["3-otlichiya"] = page(3, T, f'''
<div class="abs kicker" style="top:330px">ЧЕМ МЫ ОТЛИЧАЕМСЯ</div>
<div class="abs h" style="top:390px;font-size:120px">Только<br><span>практика</span></div>
<div class="abs panel" style="top:690px">
  <div class="row"><span class="n">01</span><div><h3>Результат, а не сертификат</h3><p>Готовая работа, которую можно показать</p></div></div>
  <div class="row"><span class="n">02</span><div><h3>Живые эфиры с преподавателями</h3><p>Делаем вместе, а не смотрим записи в одиночку</p></div></div>
  <div class="row"><span class="n">03</span><div><h3>Без воды</h3><p>Ни «как заработать миллион», ни лекций ради лекций</p></div></div>
  <div class="row"><span class="n">04</span><div><h3>Честно про всё до оплаты</h3><p>Что понадобится и сколько это стоит, вы знаете заранее</p></div></div>
</div>
''', glow=("-260px","900px","-320px","200px"))

# 4. что есть сейчас
CARDS["4-chto-est"] = page(4, T, f'''
<div class="abs kicker" style="top:330px">С ЧЕГО НАЧАТЬ</div>
<div class="abs h" style="top:390px;font-size:120px">Что есть<br><span>сейчас</span></div>
<div class="abs panel" style="top:690px">
  <div class="row"><i>{CHECK}</i><div><h3>Курс «Вайбкодинг»</h3><p>Две недели, 5 живых эфиров, заявки с сайта в Telegram, проверка домашних работ</p></div></div>
  <div class="row"><i>{CHECK}</i><div><h3>Гайд «Вайбкодинг с нуля»</h3><p>PDF для полного нуля: что это, что можно сделать и как начать</p></div></div>
</div>
<div class="abs marker" style="left:76px;top:1320px;font-size:64px;color:{PINK};transform:rotate(-5deg)">more<br>coming soon</div>
<div class="abs" style="left:620px;top:1342px;font-size:32px;font-weight:600;color:#c9c9d2;line-height:1.35">Скоро дизайн<br>и другие направления</div>
<div class="abs" style="left:68px;right:68px;top:1540px;border-radius:44px;background:{TEAL};color:#000;padding:38px 50px">
  <div style="font-size:30px;font-weight:700;opacity:.7;margin-bottom:8px">Подробности и запись</div>
  <div style="font-size:46px;font-weight:900;letter-spacing:-1px">genzschool.vercel.app</div>
  <div style="font-size:34px;font-weight:700;margin-top:6px">Telegram @ameerqan</div>
</div>
''')

# обложка для кружка актуального
CARDS["0-oblozhka"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0}}html,body{{width:1080px;height:1920px;background:#000;overflow:hidden}}
.c{{position:absolute;left:190px;top:610px;width:700px;height:700px;border-radius:50%;
 background:radial-gradient(circle at 30% 25%,#1a1a20,#0b0b0e 70%);box-shadow:inset 0 0 0 6px {TEAL};display:grid;place-items:center}}
.c svg{{width:380px;height:380px}}
.s{{position:absolute;width:120px;height:120px;left:640px;top:650px}}
</style></head><body><div class="c">{LOGO}</div><div class="s">{SPARK}</div></body></html>'''

for name, html in CARDS.items():
    src = HERE / f"{name}.html"
    src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--window-size=1080,1920", "--force-device-scale-factor=1", "--virtual-time-budget=6000",
                    f"--screenshot={HERE / (name + '.png')}", src.as_uri()], check=True, capture_output=True)
    print("готово:", name + ".png")
