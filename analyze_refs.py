import re
import os

files = ['mathematical_framework.html', 'biology_of_llm.html', 'in_context_learning_and_induction_heads.html']

for f in files:
    path = os.path.join(r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr', f)
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # check for bibliography entries or translations
    print(f"--- {f} ---")
    
    # find where bibliography starts
    bib_idx = text.find('id="references"')
    if bib_idx == -1:
        bib_idx = text.find('<d-bibliography')
        
    if bib_idx != -1:
        print("Bibliography section exists")
        
    # check if there are any translated references (often inside <d-bibliography> or in a list)
    # usually references contain things like "저널", "출판사", "페이지" if they were translated
    kr_terms = ['저널', '출판사', '페이지', '년도', '학회', '학술대회']
    found = []
    
    if bib_idx != -1:
        bib_text = text[bib_idx:]
        for term in kr_terms:
            if term in bib_text:
                found.append(term)
                
    if found:
        print("POSSIBLE KOREAN TRANSLATION IN REFERENCES:", found)
    else:
        print("References appear to be in English.")
        
    print()
