from array import *

a1 = array('i', [10,28,93,28,83,287,83])


a1.append(29)
print(a1.index(287))
a1.extend([29])
a1.index(93)
a1.insert(0, 92)
a1.pop(2)
a1.remove(83)
a1.reverse()

for i in range(len(a1)):
    print(a1[i], end=' ')


l1 = [29,92,82,37]
l1.append(25)
l1.insert(3,19)
l1.extend([27,93])
l1.pop()
l1.remove(19)
l1.sort()
l1.reverse()
print(l1)