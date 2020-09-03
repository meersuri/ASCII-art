# number of columns in the grid 
n = 100
# tree divided into three parts - top, leaves and trunk
top = [[chr(42)]]
top_start = n//2

leaves = [['/', chr(42), '\\'],
         ['/','\'', chr(176), '\'', '\\'],
         ['>', '/', '\\','/', '\\','/','<'],
         ['/','\'', chr(164),'\'', chr(164),'\'', chr(164),'\'', '\\'],
         ['/','\'', chr(176),'\'', chr(176),'\'', chr(176),'\'', chr(176),'\'', '\\'],
         ['>', '/', '\\','/', '\\','/', '\\','/', '\\''/','\\''/','<'],
         ['/','\'', chr(164),'\'', chr(164),'\'', chr(164),'\'', chr(164),'\'',chr(164),
          '\'',chr(164),'\'', '\\'],
         ['^','O','^','O','^','O','^','O','^','O','^','O','^','O','^','O','^']]
leaves_start = n//2 - 1

trunk = [['|', '~', '|'],
         ['[', '_', ']'],
         ]
trunk_start = n//2 - 1
#print top
for i in range(len(top)):
    for j in range(top_start):
        print(" ", end = "")
    for x in top[i]:
         print(x, end = "")
    for j in range(n - (top_start + len(top[i]))):
        print(" ", end = "")
    print()
#print leaves        
for i in range(len(leaves)):
    for j in range(leaves_start - i):
        print(" ", end = "")
    for x in leaves[i]:
         print(x, end = "")
    for j in range(n - (leaves_start + len(leaves[i]))):
        print(" ", end = "")
    print()
#print trunk    
for i in range(len(trunk)):
    for j in range(trunk_start):
        print(" ", end = "")
    for x in trunk[i]:
         print(x, end = "")
    for j in range(n - (trunk_start + len(trunk[i]))):
        print(" ", end = "")
    print()