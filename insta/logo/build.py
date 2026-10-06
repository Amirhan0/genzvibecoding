"""Логотип gen z school: python3 build.py"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TEAL, PINK = "#81DAD3", "#FF2E9F"

MARK = f'''<svg class="mark" viewBox="0 0 120 120"><path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" fill="{TEAL}"/><rect x="33" y="42" width="11" height="24" rx="5.5" fill="#000"/><rect x="76" y="40" width="11" height="24" rx="5.5" fill="#000"/><path d="M34 78 Q60 104 86 76" fill="none" stroke="#000" stroke-width="11" stroke-linecap="round"/></svg>'''
SPARK = f'<svg class="spark" viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{PINK}"/></svg>'

def doc(w, h, inner, bg="#000"):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700;900&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{w}px;height:{h}px;background:{bg};overflow:hidden}}
body{{display:grid;place-items:center;font-family:'Unbounded',sans-serif;color:#fff}}
.m{{position:relative;flex:none}} .m .mark{{width:100%;height:100%;display:block}}
.m .spark{{position:absolute;width:34%;height:34%;top:-9%;right:-11%}}
.w{{font-weight:900;letter-spacing:-.045em;line-height:.9}} .w b{{color:{TEAL};font-weight:900}}
</style></head><body>{inner}</body></html>'''

VARIANTS = {
    # квадрат: знак сверху, название в две строки
    "logo-square": (1080, 1080, '''<div style="display:flex;flex-direction:column;align-items:center;gap:70px">
      <div class="m" style="width:380px;height:380px">MARK SPARK</div>
      <div class="w" style="font-size:150px;text-align:center">gen z<br><b>school</b></div></div>'''),
    # в строку: для шапок, обложек, презентаций
    "logo-horizontal": (2000, 700, '''<div style="display:flex;align-items:center;gap:70px">
      <div class="m" style="width:330px;height:330px">MARK SPARK</div>
      <div class="w" style="font-size:190px;white-space:nowrap">gen z <b>school</b></div></div>'''),
    # аватарка: только знак, с запасом под круглую обрезку
    "avatar": (1080, 1080, '''<div class="m" style="width:560px;height:560px;margin-top:30px">MARK SPARK</div>'''),
}

for name, (w, h, inner) in VARIANTS.items():
    inner = inner.replace("MARK", MARK).replace("SPARK", SPARK)
    for suffix, bg, extra in [("", "#000", []), ("-transparent", "transparent", ["--default-background-color=00000000"])]:
        if name == "avatar" and suffix: continue
        src = HERE / f"{name}{suffix}.html"
        src.write_text(doc(w, h, inner, bg), encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                        f"--window-size={w},{h}", "--force-device-scale-factor=1", "--virtual-time-budget=5000",
                        *extra, f"--screenshot={HERE / (name + suffix + '.png')}", src.as_uri()],
                       check=True, capture_output=True)
        src.unlink()
        print("готово:", f"{name}{suffix}.png")
