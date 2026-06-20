import re

with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="architecture-attn-independent"')
end = text.find('id="zero-layer-transformers"')

with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\temp_section.txt', 'w', encoding='utf-8') as f:
    f.write(text[start:end])
