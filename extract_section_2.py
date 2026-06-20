import re

with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('잔차 스트림(Residual Stream)은 고차원 벡터 공간이다')
end = text.find('7', text.find('일종의 \'메모리 관리\' 역할을 수행하는데')) + 500

text_section = text[start:end]
text_no_templates = re.sub(r'<template.*?</template>', '', text_section, flags=re.DOTALL)

with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\temp_section_2.txt', 'w', encoding='utf-8') as f:
    f.write(text_no_templates)
