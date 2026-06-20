import re

with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('잔차 스트림(Residual Stream)은 고차원 벡터 공간입니다.')
if start == -1:
    print('Failed to find replacement text')
else:
    end = text.find('7', text.find('메모리 관리(memory management)\' 역할')) + 500
    text_section = text[start:end]
    text_no_templates = re.sub(r'<template.*?</template>', '', text_section, flags=re.DOTALL)
    
    with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\temp_section_check_2.txt', 'w', encoding='utf-8') as f:
        f.write(text_no_templates)
