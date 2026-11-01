"""Prancha de contato: python3 -I sheet.py <dir-png> <saida.png> <largura-miniatura> [Comp ...]"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

src, out, tw = sys.argv[1], sys.argv[2], int(sys.argv[3])
names = sys.argv[4:] or sorted(f[:-4] for f in os.listdir(src) if f.endswith('.png'))
imgs = []
for n in names:
    p = os.path.join(src, n + '.png')
    if not os.path.exists(p):
        continue
    im = Image.open(p).convert('RGB')
    s = tw / im.width
    imgs.append((n, im.resize((tw, int(im.height * s)), Image.LANCZOS)))
cols = min(4, len(imgs))
rows = [imgs[i:i + cols] for i in range(0, len(imgs), cols)]
pad, lab = 16, 26
H = sum(max(im.height for _, im in r) + lab + pad for r in rows) + pad
W = cols * (tw + pad) + pad
sheet = Image.new('RGB', (W, H), (120, 120, 126))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
except Exception:
    font = ImageFont.load_default()
y = pad
for r in rows:
    x = pad
    for n, im in r:
        d.text((x, y), n, fill=(255, 255, 255), font=font)
        sheet.paste(im, (x, y + lab))
        x += tw + pad
    y += max(im.height for _, im in r) + lab + pad
sheet.save(out)
print(out, sheet.size)
