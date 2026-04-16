import os
import json

def scan_docs():
    files = []
    for root, dirs, filenames in os.walk('.'):
        for f in filenames:
            if f.endswith('.md'):
                path = os.path.join(root, f).replace('\\', '/').replace('./', '')
                files.append(path)
    
    with open('index.json', 'w', encoding='utf-8') as f:
        json.dump(files, f, indent=2)
    
    print(f"{len(files)} fichiers trouvés")

if __name__ == '__main__':
    scan_docs()