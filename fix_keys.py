import os, re

base = r'd:\Semester 4 intern\Priyadharshini-Codeboosters-Internship-2026\Phase2'

for fname in os.listdir(base):
    if not fname.endswith('.ipynb'):
        continue
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(r'gsk_[A-Za-z0-9]+', 'xxxxxxxxxxxxxx', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    remaining = re.findall(r'gsk_[A-Za-z0-9]+', new_content)
    print(fname, '-> remaining:', remaining)

print('All done!')
