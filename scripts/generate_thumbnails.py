import os
import argparse
from PIL import Image, ImageDraw, ImageFont

def generate(input_img, out_dir, title="SUNSET LOUNGE", subtitle="DEEP ORGANIC HOUSE"):
    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(input_img).convert("RGB")
    target_w, target_h = 1280, 720
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h

    if img_ratio > target_ratio:
        new_w = int(img.height * target_ratio)
        left = (img.width - new_w) // 2
        img_cropped = img.crop((left, 0, left + new_w, img.height))
    else:
        new_h = int(img.width / target_ratio)
        top = (img.height - new_h) // 2
        img_cropped = img.crop((0, top, img.width, top + new_h))

    clean = img_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    clean.save(os.path.join(out_dir, "thumbnail_clean.jpg"), quality=95)
    print("Saved thumbnail_clean.jpg")

    badged = clean.copy()
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    o_draw = ImageDraw.Draw(overlay)
    for y in range(400, 720):
        alpha = int(160 * ((y - 400) / 320.0))
        o_draw.line([(0, y), (target_w, y)], fill=(10, 8, 15, alpha))

    badged = Image.alpha_composite(badged.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(badged)

    font_large = font_sub = font_badge = ImageFont.load_default()
    for fp in ["C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(fp):
            font_large = ImageFont.truetype(fp, 68)
            font_sub = ImageFont.truetype(fp, 32)
            font_badge = ImageFont.truetype(fp, 24)
            break

    draw.rounded_rectangle([48, 48, 290, 94], radius=12, fill=(20, 20, 30, 200), outline=(255, 180, 100, 180), width=2)
    draw.text((68, 58), "SONDER SOUNDS", fill=(255, 235, 200), font=font_badge)
    draw.text((48, 490), title, fill=(255, 255, 255), font=font_large)
    draw.text((48, 570), subtitle, fill=(255, 205, 120), font=font_sub)
    draw.rounded_rectangle([1080, 630, 1230, 678], radius=8, fill=(15, 15, 20, 220), outline=(255, 255, 255, 100), width=1)
    draw.text((1115, 642), "43 MIN", fill=(255, 255, 255), font=font_badge)

    badged.save(os.path.join(out_dir, "thumbnail_with_badge.jpg"), quality=95)
    print("Saved thumbnail_with_badge.jpg")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default=".")
    parser.add_argument("--title", default="SUNSET LOUNGE")
    parser.add_argument("--sub", default="DEEP ORGANIC HOUSE")
    args = parser.parse_args()
    generate(args.input, args.output, args.title, args.sub)
