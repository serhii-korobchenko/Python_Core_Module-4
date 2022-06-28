""" from pathlib import Path # Error?

p = Path('D:\PYTHON\Python_Core_Module-4')    # p Указывает на папку /home/user/Downloads

#p = Path()  # p Указывает на папку из которой был запущен Python

print(p.parent)
print(p.name)
print(p.suffix)
print(p.exists())
print(p.is_dir())
print(p.is_file()) """

from pathlib import Path

p = Path('D:\PYTHON\Python_Core_Module-4')    # p Указывает на папку /home/user/Downloads
for i in p.iterdir():
    print(i.name)   # Выведет в цикле имена всех папок и файлов в /home/user/Downloads


