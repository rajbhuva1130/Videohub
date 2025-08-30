# backend/fix_blueprints.py
import os, re, shutil

root = os.path.join(os.getcwd(), 'controllers')
# matches Blueprint(__name__, 'someName' , optional-rest) and captures the string name and the rest
pattern = re.compile(r"Blueprint\(\s*__name__\s*,\s*(['\"])([^'\"\)]+)\1(.*?)\)", re.S)

changed = []
for dirpath, _, filenames in os.walk(root):
    for fn in filenames:
        if not fn.endswith('.py'):
            continue
        path = os.path.join(dirpath, fn)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        def repl(m):
            quote = m.group(1)
            name = m.group(2)
            rest = m.group(3) or ''
            # produce: Blueprint("name", __name__ rest)
            return f"Blueprint({quote}{name}{quote}, __name__{rest})"
        new_text = pattern.sub(repl, text)
        if new_text != text:
            shutil.copy(path, path + '.bak')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            changed.append(path)

if not changed:
    print("No fixes needed.")
else:
    print("Fixed files (backups saved with .bak):")
    for p in changed:
        print(" -", p)
