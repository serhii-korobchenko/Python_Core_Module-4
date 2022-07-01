""" Напишите функцию parse_folder, она принимает единственный параметр path, 
который является объектом Path. Функция должна просканировать директорию path и 
вернуть кортеж из двух списков. Первый — это список файлов внутри директории, 
второй — список директорий.

Пример вывода функции:

(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 
 'module-05', 'module-06', 'module-07',
  'module-08', 'module-09', 'module-10', 'module-11', 'module-12 """

from pathlib import Path

def parse_folder(path):
    files = []
    folders = []

    #p = Path (path) # p Указывает на папку /home/user/Downloads
    for i in Path(path).iterdir():
        #print(i.name)  # Выведет в цикле имена всех папок и файлов в /home/user/Downloads
        if i.is_dir():
            folders.append(i.name)
        elif i.is_file():
             files.append(i.name)
    joint_list = [files, folders]
    joint_tuple = tuple(joint_list)
    
    print (joint_tuple)  
    return joint_tuple    
            
    #return files, folders

#parse_folder('D:\GoIT')
parse_folder('/PYTHON/Python_Core_Module-4/Home Work')

