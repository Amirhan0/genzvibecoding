"""Посты для ленты Instagram 1080x1350: python3 build.py"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T, P = "#81DAD3", "#FF2E9F"
LOGO = f'<svg viewBox="0 0 120 120"><path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" fill="{T}"/><rect x="33" y="42" width="11" height="24" rx="5.5" fill="#000"/><rect x="76" y="40" width="11" height="24" rx="5.5" fill="#000"/><path d="M34 78 Q60 104 86 76" fill="none" stroke="#000" stroke-width="11" stroke-linecap="round"/></svg>'
SPARK = f'<svg viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{P}"/></svg>'

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;background:#000;overflow:hidden}}
body{{position:relative;font-family:Montserrat,sans-serif;color:#fff}}
.a{{position:absolute}}
.g1{{width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(129,218,211,.17),transparent 62%)}}
.g2{{width:850px;height:850px;border-radius:50%;background:radial-gradient(circle,rgba(255,46,159,.16),transparent 62%)}}
.brand{{left:70px;top:64px;display:flex;align-items:center;gap:16px;font-size:34px;font-weight:800}}
.brand svg{{width:56px;height:56px}} .brand b{{color:{T}}}
.cnt{{right:70px;top:76px;font-size:28px;font-weight:700;color:#77777f}} .cnt b{{color:#fff}}
.k{{left:74px;font-size:26px;letter-spacing:7px;color:{T};font-weight:700}}
.h{{left:66px;right:66px;font-weight:900;letter-spacing:-4px;line-height:.98}}
.h span{{color:{T}}} .h i{{font-style:normal;color:{P}}}
.t{{left:74px;right:74px;font-size:38px;line-height:1.4;color:#cfcfd8;font-weight:500}}
.t b{{color:#fff;font-weight:700}}
.box{{left:66px;right:66px;border-radius:36px;background:#0f0f12;box-shadow:inset 0 0 0 2px #24242a;padding:38px 44px}}
.lab{{font-size:24px;font-weight:800;letter-spacing:4px;margin-bottom:16px}}
.mk{{font-family:'Permanent Marker',cursive;text-transform:uppercase;line-height:.95}}
.foot{{left:70px;right:70px;bottom:58px;display:flex;justify-content:space-between;font-size:24px;color:#77777f;font-weight:600}}
.foot b{{color:{T}}}
.big{{font:900 220px/1 Montserrat;color:{P};letter-spacing:-8px}}
"""

def page(inner, n=None, total=None, swipe=True, glow=("-260px","80px","-300px","760px")):
    foot_r = '<span>листайте <b>→</b></span>' if (n and n < total and swipe) else '<span>@genz.school.kz</span>'
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&family=Permanent+Marker&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="a g1" style="right:{glow[0]};top:{glow[1]}"></div><div class="a g2" style="left:{glow[2]};top:{glow[3]}"></div>
<div class="a brand">{LOGO}<span>gen z <b>school</b></span></div>
{f'<div class="a cnt"><b>{n}</b> / {total}</div>' if n else ''}
{inner}
<div class="a foot"><span>no thoughts, just ship it</span>{foot_r}</div>
</body></html>'''

POSTS = {}

# ---------- карусель: почему мы открыли школу ----------
N = 5
POSTS["1-1"] = page(f'''
<div class="a k" style="top:250px">НАША ИСТОРИЯ</div>
<div class="a h" style="top:300px;font-size:120px">Почему мы<br>открыли<br><span>gen z school</span></div>
<div class="a" style="right:80px;top:880px;width:300px;height:300px;transform:rotate(-8deg)">{LOGO}<div style="position:absolute;width:90px;height:90px;top:-14px;right:-18px">{SPARK}</div></div>
''', 1, N)

POSTS["1-2"] = page(f'''
<div class="a k" style="top:250px">ЧТО НАС БЕСИЛО</div>
<div class="a h" style="top:300px;font-size:104px">Часы теории.<br><i>Ноль</i><br>результата.</div>
<div class="a t" style="top:740px">Многие курсы устроены одинаково: длинные записи, сертификат в конце и ощущение, что вы так ничего и не сделали.</div>
''', 2, N, glow=("-200px","700px","-300px","60px"))

ROWS = ""
for i, (x, y) in enumerate([("лекции в записи", "живые эфиры"), ("сертификат", "готовая работа"), ("сам разбирайся", "проверяем каждую")]):
    line = "border-bottom:2px solid #1e1e24;" if i < 2 else ""
    ROWS += (f'<div style="display:flex;gap:26px;align-items:center;padding:26px 0;{line}">'
             f'<span style="font-size:30px;color:#6b6b75;text-decoration:line-through;flex:1">{x}</span>'
             f'<span style="font-size:44px;color:{P}">→</span>'
             f'<span style="font-size:38px;font-weight:800;flex:1">{y}</span></div>')
POSTS["1-3"] = page(f'''
<div class="a k" style="top:250px">ПОЭТОМУ МЫ</div>
<div class="a h" style="top:300px;font-size:104px">Сделали<br>наоборот</div>
<div class="a box" style="top:600px;padding:14px 44px">{ROWS}</div>
''', 3, N)

POSTS["1-4"] = page(f'''
<div class="a k" style="top:250px">А ПОЧЕМУ GEN Z</div>
<div class="a h" style="top:300px;font-size:100px">Поколение,<br>которое<br><span>не ждёт</span></div>
<div class="a t" style="top:760px">Не ждёт «идеального момента», разрешения или пятилетнего диплома. Учится на ходу и сразу делает.</div>
<div class="a t" style="top:1030px;color:{T};font-weight:700">И неважно, сколько вам лет: gen z это про подход.</div>
''', 4, N, glow=("-200px","600px","-300px","100px"))

POSTS["1-5"] = page(f'''
<div class="a k" style="top:250px">ЧТО ДАЛЬШЕ</div>
<div class="a h" style="top:300px;font-size:104px">Начинаем<br>с <span>вайбкодинга</span>,<br>дальше <i>дизайн</i></div>
<div class="a t" style="top:780px">А какое направление будет третьим, решаете вы.</div>
<div class="a box" style="top:960px;text-align:center"><div style="font-size:40px;font-weight:800">Напишите <span style="color:{T}">«ХОЧУ»</span> в директ</div><div style="font-size:30px;color:#a6a6b2;margin-top:10px">расскажем про ближайший поток</div></div>
''', 5, N)

# ---------- одиночные ----------
POSTS["2-mif"] = page(f'''
<div class="a k" style="top:250px">МИФ</div>
<div class="a h" style="top:300px;font-size:104px;color:#6b6b75;text-decoration:line-through;text-decoration-color:{P};text-decoration-thickness:5px">«Чтобы начать,<br>нужен опыт»</div>
<div class="a k" style="top:650px;color:{P}">ПРАВДА</div>
<div class="a h" style="top:700px;font-size:96px">Нужно <span>желание</span><br>и пара вечеров<br>в неделю</div>
<div class="a t" style="top:1080px;font-size:34px">Все наши направления рассчитаны на тех, кто начинает с нуля.</div>
''', glow=("-200px","500px","-300px","100px"))

POSTS["3-pravila"] = page(f'''
<div class="a k" style="top:250px">КАК МЫ УЧИМ</div>
<div class="a h" style="top:300px;font-size:110px">3 правила<br><span>gen z school</span></div>
<div class="a box" style="top:560px;padding:20px 44px">
''' + "".join(f'<div style="display:flex;gap:30px;padding:30px 0;{"border-bottom:2px solid #1e1e24;" if i<2 else ""}"><span style="font:900 56px/1 Montserrat;color:{P};flex:none;width:80px">0{i+1}</span><div><div style="font-size:42px;font-weight:800;margin-bottom:8px">{a}</div><div style="font-size:31px;color:#a6a6b2;line-height:1.35">{b}</div></div></div>'
  for i,(a,b) in enumerate([("Результат, а не сертификат","В конце у вас готовая работа"),("Делаем вместе","Живые эфиры, а не записи в одиночку"),("Проверяем сами","Каждую домашнюю работу, не бот")])) + '</div>')

POSTS["4-predzapis"] = page(f'''
<div class="a" style="left:66px;top:230px;background:{P};color:#fff;font-weight:900;font-size:30px;letter-spacing:3px;padding:16px 28px;border-radius:16px;transform:rotate(-3deg)">ПРЕДЗАПИСЬ ОТКРЫТА</div>
<div class="a h" style="top:360px;font-size:118px">Чему хотите<br><span>научиться?</span></div>
<div class="a" style="left:66px;right:66px;top:690px;display:flex;flex-direction:column;gap:18px">
  <div class="box" style="position:static;display:flex;justify-content:space-between;align-items:center"><div style="font-size:44px;font-weight:800">Вайбкодинг</div><div style="background:{T};color:#000;font-weight:800;font-size:24px;padding:10px 18px;border-radius:99px">ОТКРЫТ</div></div>
  <div class="box" style="position:static;display:flex;justify-content:space-between;align-items:center"><div style="font-size:44px;font-weight:800">Дизайн</div><div style="background:{P};color:#fff;font-weight:800;font-size:24px;padding:10px 18px;border-radius:99px">СКОРО</div></div>
  <div class="box" style="position:static;display:flex;justify-content:space-between;align-items:center;background:transparent;box-shadow:inset 0 0 0 2px #3a3a42"><div style="font-size:44px;font-weight:800;color:#a6a6b2">Ваш вариант?</div><div style="font-size:30px;color:{T};font-weight:700">пишите</div></div>
</div>
<div class="a t" style="top:1140px;font-size:34px">Напишите <b>«ХОЧУ»</b> в директ</div>
''', glow=("-260px","300px","-300px","900px"))

for name, html in POSTS.items():
    src = HERE / f"{name}.html"; src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--window-size=1080,1350", "--force-device-scale-factor=1", "--virtual-time-budget=6000",
        f"--screenshot={HERE/(name+'.png')}", src.as_uri()], check=True, capture_output=True)
    src.unlink(); print("готово:", name + ".png")
