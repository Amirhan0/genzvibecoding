"""Сторис «Частые вопросы» 1080x1920: python3 build.py"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T, P = "#81DAD3", "#FF2E9F"
LOGO = f'<svg viewBox="0 0 120 120"><path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" fill="{T}"/><rect x="33" y="42" width="11" height="24" rx="5.5" fill="#000"/><rect x="76" y="40" width="11" height="24" rx="5.5" fill="#000"/><path d="M34 78 Q60 104 86 76" fill="none" stroke="#000" stroke-width="11" stroke-linecap="round"/></svg>'
SPARK = f'<svg viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{P}"/></svg>'

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;background:#000;overflow:hidden}}
body{{position:relative;font-family:Montserrat,sans-serif;color:#fff}}
.a{{position:absolute}}
.g1{{width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,rgba(129,218,211,.18),transparent 62%)}}
.g2{{width:950px;height:950px;border-radius:50%;background:radial-gradient(circle,rgba(255,46,159,.17),transparent 62%)}}
.brand{{left:72px;top:74px;display:flex;align-items:center;gap:18px;font-size:38px;font-weight:800}}
.brand svg{{width:64px;height:64px}} .brand b{{color:{T}}}
.cnt{{right:72px;top:88px;font-size:30px;font-weight:700;color:#77777f}} .cnt b{{color:#fff}}
.k{{left:76px;font-size:28px;letter-spacing:8px;color:{T};font-weight:700}}
.h{{left:68px;right:68px;font-weight:900;letter-spacing:-5px;line-height:.98}}
.h span{{color:{T}}}
.q{{left:68px;right:68px;border-radius:44px 44px 44px 10px;background:#17171c;box-shadow:inset 0 0 0 2px #2a2a31;padding:48px 52px;font-size:62px;font-weight:800;line-height:1.15;letter-spacing:-1px}}
.ans{{left:68px;right:68px;border-radius:44px 44px 10px 44px;background:{T};color:#000;padding:50px 52px}}
.ans .l{{font-size:26px;font-weight:800;letter-spacing:5px;opacity:.6;margin-bottom:16px}}
.ans .t{{font-size:50px;font-weight:700;line-height:1.3}}
.tag{{left:0;right:0;bottom:70px;text-align:center;font-size:26px;letter-spacing:10px;color:#9a9aa6}}
"""
def page(inner, n, total, glow):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="a g1" style="right:{glow[0]};top:{glow[1]}"></div><div class="a g2" style="left:{glow[2]};top:{glow[3]}"></div>
<div class="a brand">{LOGO}<span>gen z <b>school</b></span></div>
<div class="a cnt"><b>{n}</b> / {total}</div>
{inner}
<div class="a tag">no thoughts, just ship it</div></body></html>'''

QA = [
    ("А если у меня ноль опыта?", "Отлично. Все наши направления рассчитаны на тех, кто начинает с нуля."),
    ("Обязательно включать камеру?", "Нет. Можно участвовать без камеры и микрофона, а вопросы писать в чат."),
    ("Подойдёт ли девушкам?", "Да, конечно! Школа для всех, кто хочет научиться создавать своё."),
    ("Сколько времени нужно?", "Пара вечеров в неделю: эфир и немного практики после него."),
]
TOT = len(QA) + 2
S = {}
S["1"] = page(f'''
<div class="a k" style="top:420px">ВЫ СПРАШИВАЛИ</div>
<div class="a h" style="top:480px;font-size:160px">Частые<br><span>вопросы</span></div>
<div class="a" style="left:0;right:0;top:960px;text-align:center;font:900 520px/1 Montserrat;color:{P}">?</div>
''', 1, TOT, ("-300px","200px","-320px","1100px"))
for i, (q, a) in enumerate(QA, start=2):
    S[str(i)] = page(f'''
<div class="a k" style="top:430px">ВОПРОС {i-1}</div>
<div class="a q" style="top:500px">{q}</div>
<div class="a ans" style="top:900px"><div class="l">ОТВЕТ</div><div class="t">{a}</div></div>
<div class="a" style="right:110px;top:1380px;width:150px;height:150px;transform:rotate(12deg)">{SPARK}</div>
''', i, TOT, ("-300px", f"{300+i*60}px", "-320px", "1200px"))
S[str(TOT)] = page(f'''
<div class="a k" style="top:420px">ОСТАЛИСЬ ВОПРОСЫ?</div>
<div class="a h" style="top:480px;font-size:140px">Спросите<br><span>нас</span></div>
<div class="a" style="left:68px;right:68px;top:900px;font-size:44px;line-height:1.4;color:#cfcfd8;font-weight:500">Напишите в директ, ответим лично. Или оставьте заявку на сайте.</div>
<div class="a ans" style="top:1220px;text-align:center"><div class="t" style="font-weight:900;font-size:54px">Написать в директ</div></div>
''', TOT, TOT, ("-300px","700px","-320px","200px"))

for n, html in S.items():
    src = HERE / f"faq-{n}.html"; src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--window-size=1080,1920", "--force-device-scale-factor=1", "--virtual-time-budget=6000",
        f"--screenshot={HERE/f'faq-{n}.png'}", src.as_uri()], check=True, capture_output=True)
    src.unlink(); print("готово:", f"faq-{n}.png")
