from enum import Enum
import subprocess 
import sys

class Item(Enum):
    Num=0
    Value=1
    Size=2
    Type=3
    Bind=4
    Vis=5
    Ndx=6
    Name=7
    MAX=8

func = {}
obj = {}
func_dup = []
obj_dup = []
start=0

if len(sys.argv) != 3:
    print("Please give 2 arguments")

symbols1 = subprocess.run(['readelf', '-W', '-s', sys.argv[1]], capture_output=True, text=True).stdout
symbols2 = subprocess.run(['readelf', '-W', '-s', sys.argv[2]], capture_output=True, text=True).stdout

for l in symbols1.split('\n'):
    if ".dynsym" in l:
        start=1
    elif ".symtab" in l:
        start=0
    if not start:
        continue

    items = l.split()
    if len(items) != Item.MAX.value:
        continue
    if items[Item.Type.value] == "FUNC":
        func[items[Item.Name.value]]=1
    elif items[Item.Type.value] == "OBJECT":
        obj[items[Item.Name.value]]=1


for l in symbols2.split('\n'):
    if ".dynsym" in l:
        start=1
    elif ".symtab" in l:
        start=0
    if not start:
        continue

    items = l.split()
    if len(items) != Item.MAX.value:
        continue
    if items[Item.Type.value] == "FUNC":
        if items[Item.Name.value] in func:
            func_dup.append(items[Item.Name.value])
    elif items[Item.Type.value] == "OBJECT":
        if items[Item.Name.value] in obj:
            obj_dup.append(items[Item.Name.value])

print("FUNC")
for a in func_dup:
    print(a)
print("\nOBJ")
for a in obj_dup:
    print(a)


        
