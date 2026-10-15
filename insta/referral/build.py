"""Сторис «Приведи друга» 1080x1920: python3 build.py"""
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
.marker{{font-family:'Permanent Marker',cursive;line-height:.95;text-transform:uppercase}}
.g1{{width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,rgba(129,218,211,.18),transparent 62%)}}
.g2{{width:950px;height:950px;border-radius:50%;background:radial-gradient(circle,rgba(255,46,159,.17),transparent 62%)}}
.brand{{left:72px;top:74px;display:flex;align-items:center;gap:18px;font-size:38px;font-weight:800}}
.brand svg{{width:64px;height:64px}} .brand b{{color:{T}}}
.cnt{{right:72px;top:88px;font-size:30px;font-weight:700;color:#77777f}} .cnt b{{color:#fff}}
.k{{left:76px;font-size:28px;letter-spacing:8px;color:{T};font-weight:700}}
.h{{left:68px;right:68px;font-weight:900;letter-spacing:-5px;line-height:.98}}
.h span{{color:{T}}}
.card{{left:68px;right:68px;border-radius:44px;background:#0f0f12;box-shadow:inset 0 0 0 2px #24242a;padding:44px 50px}}
.card .l{{font-size:28px;font-weight:800;letter-spacing:5px;color:#8b8b98;margin-bottom:14px}}
.card .big{{font-size:96px;font-weight:900;letter-spacing:-3px;line-height:1}}
.card .big s{{font-size:52px;color:#6b6b76;font-weight:700;letter-spacing:-1px;margin-left:18px}}
.card p{{font-size:34px;color:#b9b9c4;line-height:1.35;font-weight:500;margin-top:14px}}
.row{{display:flex;gap:30px;align-items:flex-start;padding:28px 0;border-bottom:2px solid #1e1e24}}
.row:last-child{{border:0}}
.row .n{{flex:none;font:900 58px/1 Montserrat;color:{P};width:84px}}
.row h3{{font-size:46px;font-weight:800;line-height:1.15;margin-bottom:8px;letter-spacing:-1px}}
.row p{{font-size:33px;color:#a6a6b2;line-height:1.35;font-weight:500;margin:0}}
.cta{{left:68px;right:68px;border-radius:44px;background:{T};color:#000;padding:38px 50px}}
.tag{{left:0;right:0;bottom:70px;text-align:center;font-size:26px;letter-spacing:10px;color:#9a9aa6}}
"""

def page(inner, n, total, glow):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&family=Permanent+Marker&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="a g1" style="right:{glow[0]};top:{glow[1]}"></div>
<div class="a g2" style="left:{glow[2]};top:{glow[3]}"></div>
<div class="a brand">{LOGO}<span>gen z <b>school</b></span></div>
<div class="a cnt"><b>{n}</b> / {total}</div>
{inner}
<div class="a tag">no thoughts, just ship it</div>
</body></html>'''

STORIES = {}

STORIES["ref-1"] = page(f'''
<div class="a k" style="top:300px">НОВОЕ · ПРИВЕДИ ДРУГА</div>
<div class="a h" style="top:360px;font-size:132px">Зови друга —<br><span>получай<br>5 000 ₸</span></div>
<div class="a" style="right:90px;top:560px;width:200px;height:200px;transform:rotate(10deg)">{LOGO}<div style="position:absolute;width:64px;height:64px;top:-10px;right:-12px">{SPARK}</div></div>

<div class="a card" style="top:930px">
  <div class="l">ДРУГУ</div>
  <div class="big">35 000 ₸<s>40 000</s></div>
  <p>Скидка 5 000 ₸ на курс вайбкодинга по твоей ссылке</p>
</div>
<div class="a card" style="top:1290px;box-shadow:inset 0 0 0 3px {T}">
  <div class="l" style="color:{T}">ТЕБЕ</div>
  <div class="big">+5 000 ₸</div>
  <p>За каждого друга, который оплатил курс. Сколько друзей — столько и выплат</p>
</div>
<div class="a" style="left:76px;top:1655px;font-size:44px;font-weight:900;font-style:italic;letter-spacing:-1px;color:{P};transform:rotate(-3deg)">учиться самому не обязательно ✦</div>
''', 1, 2, ("-300px", "150px", "-320px", "1150px"))

STORIES["ref-2"] = page(f'''
<div class="a k" style="top:300px">КАК ЭТО РАБОТАЕТ</div>
<div class="a h" style="top:360px;font-size:120px">Три<br><span>шага</span></div>

<div class="a card" style="top:660px;padding:30px 50px">
  <div class="row"><span class="n">01</span><div><h3>Возьми ссылку</h3><p>На сайте в блоке «Приведи друга» впиши свой Telegram</p></div></div>
  <div class="row"><span class="n">02</span><div><h3>Отправь другу</h3><p>Он оставляет заявку по ссылке — или пишет нам, что от тебя</p></div></div>
  <div class="row"><span class="n">03</span><div><h3>Получи 5 000 ₸</h3><p>Друг оплатил курс — переводим тебе на карту</p></div></div>
</div>

<div class="a cta" style="top:1400px">
  <div style="font-size:30px;font-weight:700;opacity:.7;margin-bottom:8px">Ссылка и условия</div>
  <div style="font-size:46px;font-weight:900;letter-spacing:-1px">genzschool.vercel.app</div>
  <div style="font-size:34px;font-weight:700;margin-top:6px">вопросы — Telegram @ameerqan</div>
</div>
''', 2, 2, ("-260px", "900px", "-320px", "200px"))

for name, html in STORIES.items():
    src = HERE / f"{name}.html"
    src.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--window-size=1080,1920", "--force-device-scale-factor=1", "--virtual-time-budget=6000",
                    f"--screenshot={HERE / (name + '.png')}", src.as_uri()], check=True, capture_output=True)
    src.unlink()
    print("готово:", name + ".png")
