import os
from PIL import Image
import pillow_avif
import argparse

def batch_convert(source_dir, dest_dir, quality=80):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            source_path = os.path.join(source_dir, filename)
            base_name = os.path.splitext(filename)[0]
            dest_path = os.path.join(dest_dir, f"{base_name}.avif")
            
            try:
                print(f"Converting {filename} to {base_name}.avif...")
                with Image.open(source_path) as img:
                    img.save(dest_path, "AVIF", quality=quality)
                print(f"Saved: {dest_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")
        elif filename.lower().endswith('.avif'):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            try:
                print(f"Copying {filename} (already AVIF)...")
                import shutil
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {dest_path}")
            except Exception as e:
                print(f"Error copying {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch convert images to AVIF")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("destination", help="Destination directory")
    parser.add_argument("--quality", type=int, default=80, help="AVIF quality (1-100)")
    
    args = parser.parse_args()
    batch_convert(args.source, args.destination, args.quality)
