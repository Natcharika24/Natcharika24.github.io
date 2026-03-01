import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('new_styles.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

new_html = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n    </style>', html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Styles patched successfully.")
