from pathlib import Path

p1 = Path('files/ghi.txt')  # je PosixPath  =  WindowsPath
print(type(p1))

if not p1.exists():
    with open(p1,'w') as file:
        file.write('Content 3')

print(p1.name)
print(p1.stem)    # file name
print(p1.suffix)  # extension

p2 = Path('Files')     # enak object kot datoteke

print(p2.iterdir())
for item in p2.iterdir():
    print(type(item))

print(list(p2.iterdir()))