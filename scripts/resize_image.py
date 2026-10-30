from pathlib import Path

from PIL import Image

# Configuration
image_dir = Path(
    r"C:\\Users\jian.tay\OneDrive - Van Andel Institute\QuPath Screen\other"
)
output_dir = Path(r"../images/qupath/new")
quality_setting = 85
output_size = 0.8
crop_margin = 0

fn_prefix = "qupath_tips_"

output_dir.mkdir(parents=True, exist_ok=True)


total_items = len(list(image_dir.iterdir()))

# Find all PNG/JPG images and sort them chronologically
images = sorted(image_dir.glob("*.png"), key=lambda p: p.stat().st_mtime)
# images = sorted(image_dir.glob("*.[pj][pn][g]"), key=lambda p: p.stat().st_mtime)

print(f"Found {len(images)} images to process...")

for index, img_path in enumerate(images, start=1):
    with Image.open(img_path) as img:
        if img.width > (crop_margin * 2) and img.height > (crop_margin * 2):
            left = crop_margin
            top = crop_margin
            right = img.width - crop_margin
            bottom = img.height - crop_margin
            img = img.crop((left, top, right, bottom))

        new_width = int(img.width * output_size)
        new_height = int(img.height * output_size)

        # Resize using high-quality resampling
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # # Convert RGBA (transparent) or LA (grayscale with alpha) to RGB
        # if img_resized.mode in ("RGBA", "LA"):
        #     # Create a white background to paste the transparent image onto
        #     background = Image.new("RGB", img_resized.size, (255, 255, 255))
        #     background.paste(
        #         img_resized, mask=img_resized.split()[-1]
        #     )  # Use the alpha channel as mask
        #     img_resized = background
        # elif img_resized.mode != "RGB":
        #     img_resized = img_resized.convert("RGB")

        # New clean filename
        new_filename = f"{fn_prefix}{index}.png"
        output_path = output_dir / new_filename

        # Save optimized image
        img_resized.save(output_path, optimize=True, quality=quality_setting)
        print(f"Resized & Renamed: {img_path.name} -> {output_path!s}")

print("All images processed successfully!")
