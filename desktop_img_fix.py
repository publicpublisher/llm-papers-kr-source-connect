import os
import glob

css_fix = """
<style id="desktop-img-fix">
/* Desktop Image Fix */
@media (min-width: 768px) {
    .gdoc-image, figure {
        grid-column: text !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    .gdoc-image img, figure img {
        width: auto !important;
        max-width: 100% !important;
        height: auto !important;
    }
}
</style>
"""

def fix_all_html():
    files = glob.glob('**/*.html', recursive=True)
    count = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'id="desktop-img-fix"' in content:
            continue
            
        # Insert right before </head>
        if '</head>' in content:
            content = content.replace('</head>', css_fix + '\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Fixed {file}")
    
    print(f"Fixed {count} files.")

if __name__ == '__main__':
    fix_all_html()
