import os
import glob

def fix_images():
    html_files = glob.glob('**/*.html', recursive=True)
    fixed_count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace grid-column:screen with grid-column:text for .gdoc-image
        old_str = "grid-column:screen;display:block"
        new_str = "grid-column:text;display:block"
        
        # We specifically target the .gdoc-image rule
        if ".gdoc-image{" in content and "grid-column:screen" in content:
            # Safer replacement
            content = content.replace(".gdoc-image{width:min(calc(var(--img-width)/2),100%);margin-left:auto;margin-right:auto;grid-column:screen;display:block;padding-right:0}", 
                                      ".gdoc-image{width:min(calc(var(--img-width)/2),100%);margin-left:auto;margin-right:auto;grid-column:text;display:block;padding-right:0}")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
            print(f"Fixed {filepath}")
            
    print(f"Fixed {fixed_count} files.")

if __name__ == '__main__':
    fix_images()
