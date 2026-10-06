"""Обложки для «Актуального»: python3 build.py"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T, P = "#81DAD3", "#FF2E9F"
S = f'fill="none" stroke="{T}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'

ICONS = {
  "kto-my":   f'<path d="M62 2 C98 -4 126 26 118 62 C112 96 92 120 58 118 C24 116 0 94 2 58 C4 24 28 8 62 2 Z" transform="translate(2.4 2.4) scale(.16)" fill="{T}"/><rect x="7.7" y="9.1" width="1.8" height="3.8" rx=".9" fill="#000"/><rect x="14.6" y="8.8" width="1.8" height="3.8" rx=".9" fill="#000"/><path d="M7.8 14.9 Q12 19 16.2 14.6" fill="none" stroke="#000" stroke-width="1.8" stroke-linecap="round"/>',
  "kurs":     f'<rect x="3" y="4" width="18" height="13" rx="2.5" {S}/><path d="m10 8.3 4.2 2.2L10 12.7Z" fill="{T}"/><path d="M8 21h8M12 17v4" {S}/>',
  "gajd":     f'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z" {S}/><path d="M14 3v5h5" {S}/><path d="M8.5 13h7M8.5 16.5h4.5" {S}/>',
  "raboty":   f'<rect x="3" y="3" width="7.5" height="7.5" rx="2" {S}/><rect x="13.5" y="3" width="7.5" height="7.5" rx="2" {S}/><rect x="3" y="13.5" width="7.5" height="7.5" rx="2" {S}/><path d="M17.25 14v6.5M14 17.25h6.5" {S}/>',
  "otzyvy":   f'<path d="M20.5 14.6a2.6 2.6 0 0 1-2.6 2.6H8.4L3.5 21V6.2a2.6 2.6 0 0 1 2.6-2.6h11.8a2.6 2.6 0 0 1 2.6 2.6Z" {S}/><path d="m12 7.3 1.1 2.3 2.5.3-1.8 1.7.4 2.5-2.2-1.2-2.2 1.2.4-2.5-1.8-1.7 2.5-.3Z" fill="{T}"/>',
  "voprosy":  f'<circle cx="12" cy="12" r="9" {S}/><path d="M9.4 9.3a2.7 2.7 0 1 1 3.7 2.5c-.7.3-1.1.9-1.1 1.6v.6" {S}/><circle cx="12" cy="17" r="1" fill="{T}"/>',
  "kontakty": f'<path d="M21 3 3.6 10.2c-.8.3-.8 1.4 0 1.7l4.4 1.6 1.6 5.2c.2.8 1.2 1 1.8.4l2.5-2.4 4.5 3.3c.6.5 1.6.1 1.7-.7L23 4.3c.1-.9-.8-1.6-2-1.3Z" transform="translate(-.6 .4) scale(.95)" {S}/><path d="m8 13.5 9-6.3" {S}/>',
  "dizajn":   f'<path d="M12 3a9 9 0 1 0 0 18c1.2 0 1.8-.8 1.8-1.7 0-.5-.2-.9-.5-1.2-.3-.3-.5-.7-.5-1.2 0-1 .8-1.7 1.7-1.7H16a5 5 0 0 0 5-5c0-4-4-7.2-9-7.2Z" {S}/><circle cx="7.5" cy="11" r="1.2" fill="{T}"/><circle cx="10.5" cy="7.3" r="1.2" fill="{P}"/><circle cx="15" cy="7.8" r="1.2" fill="{T}"/>',
}

def page(icon):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0}}html,body{{width:1080px;height:1080px;background:#000;overflow:hidden}}
.c{{position:absolute;left:90px;top:90px;width:900px;height:900px;border-radius:50%;
 background:radial-gradient(circle at 32% 26%,#1b1b21,#09090b 72%);box-shadow:inset 0 0 0 10px {T}, 0 0 120px rgba(129,218,211,.18)}}
.i{{position:absolute;left:270px;top:270px;width:540px;height:540px}}
.s{{position:absolute;width:150px;height:150px;left:770px;top:150px}}
</style></head><body><div class="c"></div>
<svg class="i" viewBox="0 0 24 24">{icon}</svg>
<svg class="s" viewBox="0 0 36 36"><path d="M18 0 C21 11 25 15 36 18 C25 21 21 25 18 36 C15 25 11 21 0 18 C11 15 15 11 18 0 Z" fill="{P}"/></svg>
</body></html>'''

for name, icon in ICONS.items():
    src = HERE / f"{name}.html"; src.write_text(page(icon), encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--window-size=1080,1080", "--force-device-scale-factor=1", f"--screenshot={HERE/(name+'.png')}", src.as_uri()],
        check=True, capture_output=True)
    src.unlink(); print("готово:", name + ".png")
