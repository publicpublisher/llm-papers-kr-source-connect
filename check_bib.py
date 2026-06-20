with open(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<d-bibliography')
if idx == -1:
    idx = text.find('d-bibliography')
print(text[idx:idx+1000])
