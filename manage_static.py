import os
import fileinput
from bs4 import BeautifulSoup


def fix_static(path, app):
    with fileinput.FileInput(path, inplace=True, backup='.bak') as file:
        for line in file:
            if 'link' in line and 'https' not in line and 'http' not in line:
                bs = BeautifulSoup(line, 'html5lib')
                for link in bs.find_all('link', href=True):
                    if 'static' not in line:
                        print(line.replace(link['href'], '{{% static "{}/{}" %}}'.format(app, link['href'])), end='')
                    else:
                        print(line, end='')
            elif 'script' in line and 'https' not in line and 'http' not in line:
                bs = BeautifulSoup(line, 'html5lib')
                for script in bs.find_all('script', src=True):
                    if 'static' not in line:
                        print(line.replace(script['src'], '{{% static "{}/{}" %}}'.format(app, script['src'])), end='')
                    else:
                        print(line, end='')
            elif 'img' in line and 'https' not in line and 'http' not in line:
                bs = BeautifulSoup(line, 'html5lib')
                for img in bs.find_all('img', src=True):
                    if 'static' not in line:
                        print(line.replace(img['src'], '{{% static "{}/{}" %}}'.format(app, img['src'])), end='')
                    else:
                        print(line, end='')
            else:
                print(line, end='')

if __name__ == '__main__':
    work_dir = os.path.join(os.path.dirname(__file__), 'templates')
    fpath = os.path.join(work_dir, 'about.html')
    # try:
    #     os.remove(fpath)
    #     os.rename(fpath + '.bak', fpath)
    # except FileNotFoundError:
    #     pass
    fix_static(fpath, 'main_app')
    # for file in os.scandir(work_dir):
    #     fix_static(os.path.join(work_dir, file.path))