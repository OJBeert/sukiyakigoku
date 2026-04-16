import os
import re
import base64

# Path setup
html_path = 'index.html'
img_dir = 'assets/img'
os.makedirs(img_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Base64 pattern
# data:image/(jpeg|png|webp|gif|avif);base64,xxxx
pattern = r'data:image\/(?P<ext>jpeg|png|webp|gif|avif);base64,(?P<data>[A-Za-z0-9+/=]+)'

matches = list(re.finditer(pattern, content))
print(f"Found {len(matches)} images.")

# Names for images based on their order in the HTML
img_names = [
    "hero-bg", "hero-logo", "banner-1", "banner-2", "banner-3",
    "about-1", "about-2", "divider-1", "menu-1", "divider-2",
    "feat-1", "feat-2", "feat-3"
]

for i, match in enumerate(matches):
    if i >= len(img_names):
        name = f"image-{i}"
    else:
        name = img_names[i]
    
    ext = match.group('ext')
    b64_data = match.group('data')
    
    # Decode
    img_bytes = base64.b64decode(b64_data)
    
    # Save with original extension first
    filename = f"{name}.{ext}"
    file_path = os.path.join(img_dir, filename)
    with open(file_path, 'wb') as f:
        f.write(img_bytes)
    
    # Replace in HTML
    content = content.replace(match.group(0), f"assets/img/{filename}")
    print(f"Saved and replaced: {filename}")

# Save updated HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
