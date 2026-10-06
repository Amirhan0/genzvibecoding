"""Картинки превью ссылок (og:image) 1200x630: python3 build.py
Кладёт og.png и og-vibecoding.png в корень сайта."""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
SITE = HERE.parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T, P = "#81DAD3", "#FF2E9F"
LOGO = f'<svg viewBox="0 0 120 120"><path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" fill="{T}"/><rect x="33" y="42" width="11" height="24" rx="5.5" fill="#0A0A0A"/><rect x="76" y="40" width="11" height="24" rx="5.5" fill="#0A0A0A"/><path d="M34 78 Q60 104 86 76" fill="none" stroke="#0A0A0A" stroke-width="11" stroke-linecap="round"/></svg>'
SPARK = f'<svg viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{P}"/></svg>'

CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1200px;height:630px;background:#08080a;overflow:hidden}}
body{{position:relative;font-family:Inter,sans-serif;color:#fff}}
.a{{position:absolute}}
.g1{{width:760px;height:760px;border-radius:50%;right:-220px;top:-200px;background:radial-gradient(circle,rgba(129,218,211,.22),transparent 62%)}}
.g2{{width:700px;height:700px;border-radius:50%;left:-300px;bottom:-380px;background:radial-gradient(circle,rgba(255,46,159,.18),transparent 62%)}}
.brand{{left:72px;top:60px;display:flex;align-items:center;gap:14px;font:700 30px Unbounded}}
.brand svg{{width:48px;height:48px}} .brand b{{color:{T};font-weight:700}}
.k{{left:76px;top:172px;font-size:22px;letter-spacing:6px;text-transform:uppercase;color:{T};font-weight:600}}
.h{{left:70px;top:214px;font:900 92px/1 Unbounded;letter-spacing:-3px}}
.h span{{color:{T}}}
.t{{left:76px;bottom:62px;font-size:28px;color:#b9b9c4;font-weight:500}}
.t b{{color:#fff}}
.mark{{right:90px;top:170px;width:290px;height:290px;transform:rotate(-8deg)}}
.mark .s{{position:absolute;width:80px;height:80px;top:-14px;right:-20px}}
"""

def page(kicker, title, text):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600&family=Unbounded:wght@700;900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="a g1"></div><div class="a g2"></div>
<div class="a brand">{LOGO}<span>gen z <b>school</b></span></div>
<div class="a k">{kicker}</div>
<div class="a h">{title}</div>
<div class="a mark">{LOGO}<div class="s">{SPARK}</div></div>
<div class="a t">{text}</div>
</body></html>'''

IMAGES = {
    "og": page("IT, дизайн и не только", "Учим<br>создавать<br><span>с нуля</span>",
               "Живые эфиры · <b>только практика</b> · проверка каждой работы"),
    "og-vibecoding": page("курс вайбкодинга", "Сайты<br>без кода<br><span>с ИИ</span>",
                          "5 живых эфиров · <b>свой сайт в интернете</b> · 20 000 ₸"),
}

for name, html in IMAGES.items():
    src = HERE / f"{name}.html"; src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--window-size=1200,630", "--force-device-scale-factor=1", "--virtual-time-budget=6000",
        f"--screenshot={SITE/(name+'.png')}", src.as_uri()], check=True, capture_output=True)
    src.unlink(); print("готово:", name + ".png")
