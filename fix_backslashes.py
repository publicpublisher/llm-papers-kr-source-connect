import re

file_path = r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(r"\'메모리\'", "'메모리'")
text = text.replace(r"\'대역폭\'", "'대역폭'")
text = text.replace(r"\'여유(free)\'", "'여유(free)'")
text = text.replace(r"\'계산 차원\'", "'계산 차원'")
text = text.replace(r"\'병목 활성화(bottleneck activations)\'", "'병목 활성화(bottleneck activations)'")
text = text.replace(r"\'메모리 관리(memory management)\'", "'메모리 관리(memory management)'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Backslash cleanup complete.")
