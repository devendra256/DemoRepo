name = input("Enter file:")
f = open(name)
d = dict()
for i in f:
    l = i.split()
    if len(l) > 1:
        if l[0] == 'From':
            l1 = l[5].split(":")
            d[l1[0]] = d.get(l1[0],0) + 1
l2 = []
print(d)
for k,v in d.items():
    l2.append((k,v))
print(l2)
l4 = sorted(l2)
for i,j in l4:
    print(i,j)
