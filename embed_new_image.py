import os
import re
import base64

image_path = r'c:\Users\pprab\OneDrive\Desktop\mine.jpeg'
html_path = r'c:\Users\pprab\OneDrive\Desktop\Quiz Application\quiz_app\templates\quiz_app\base.html'

with open(image_path, 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

img_src = f"data:image/jpeg;base64,{b64_img}"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Use regex to find and replace the current data:image strings.
# Because there might be two instances of the image, we do a global replace
content = re.sub(r'src="data:image/[a-zA-Z0-9]+;base64,[^"]+"', f'src="{img_src}"', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("New photo (mine.jpeg) successfully embedded!")
