import os
import base64

image_path = r'c:\Users\pprab\OneDrive\Desktop\WhatsApp Image 2026-01-13 at 10.23.03_44f4a674.jpg'
html_path = r'c:\Users\pprab\OneDrive\Desktop\Quiz Application\quiz_app\templates\quiz_app\base.html'

with open(image_path, 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

img_src = f"data:image/jpeg;base64,{b64_img}"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace profile static URL with base64 string
content = content.replace("{% static 'quiz_app/images/profile.jpg' %}", img_src)

# Also do it for the logo so it appears!
content = content.replace("{% static 'quiz_app/images/logo.jpg' %}", img_src)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Base64 image embedded successfully!")
