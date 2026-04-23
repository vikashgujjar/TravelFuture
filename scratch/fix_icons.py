import os
import re

file_path = r'c:\Users\Lenovo\OneDrive\Desktop\Travel Booking\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace fa-solid fa-arrow-right
content = re.sub(r'<i\s+[^>]*class="fa-solid\s+fa-arrow-right"[^>]*></i>', '<iconify-icon icon="mdi:arrow-right"></iconify-icon>', content, flags=re.DOTALL)

# Replace fa-solid fa-map
content = re.sub(r'<i\s+[^>]*class="fa-solid\s+fa-map"[^>]*></i>', '<i class="flaticon-destination"></i>', content, flags=re.DOTALL)

# Replace fa-brands fa-youtube
content = re.sub(r'<i\s+[^>]*class="fa-brands\s+fa-youtube"[^>]*></i>', '<iconify-icon icon="mdi:youtube"></iconify-icon>', content, flags=re.DOTALL)

# Handle some specific cases that might be slightly different
content = re.sub(r'class="fa-solid\s*\n\s*fa-arrow-right"></i>', '><iconify-icon icon="mdi:arrow-right"></iconify-icon>', content)
content = re.sub(r'class="fa-solid\s*\n\s*fa-map"></i>', '><i class="flaticon-destination"></i>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
