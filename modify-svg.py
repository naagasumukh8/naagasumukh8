import re
import os

def modify_svg(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define keyframe regex pattern
    # E.g. @keyframes c0{9.93%{fill:var(--c1)}9.95%,100%{fill:var(--ce)}}
    keyframe_pattern = re.compile(
        r'@keyframes\s+(\w+)\s*\{\s*([\d\.]+)%\s*\{\s*fill\s*:\s*var\s*\(\s*(--c\d+)\s*\)\s*\}\s*([\d\.]+)%\s*,\s*100%\s*\{\s*fill\s*:\s*var\s*\(\s*(--ce)\s*\)\s*\}\s*\}'
    )

    # Define class rule regex pattern
    # E.g. .c.c0{fill:var(--c1);animation-name:c0}
    class_pattern = re.compile(
        r'\.c\.(\w+)\s*\{\s*fill\s*:\s*var\s*\(\s*--(c\d+)\s*\)\s*;\s*animation-name\s*:\s*\1\s*\}'
    )

    # Perform replacement
    def replace_keyframes(match):
        name = match.group(1)
        t1 = match.group(2)
        color = match.group(3)
        t2 = match.group(4)
        return f"@keyframes {name}{{0%,{t1}%{{fill:var(--ce)}}{t2}%,100%{{fill:var({color})}}}}"

    modified_content = keyframe_pattern.sub(replace_keyframes, content)

    def replace_classes(match):
        name = match.group(1)
        return f".c.{name}{{fill:var(--ce);animation-name:{name}}}"

    modified_content = class_pattern.sub(replace_classes, modified_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    print(f"Successfully modified {file_path}")

if __name__ == '__main__':
    # Modify both standard and dark mode SVGs in dist/
    modify_svg('dist/github-snake.svg')
    modify_svg('dist/github-snake-dark.svg')
