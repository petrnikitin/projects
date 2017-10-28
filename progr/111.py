

'''d = {}
for t in text:

    if t in text:

        d[t] = text.count(t)

m = max(d.values())
print (d)
print (m)
cont = m
print (123, cont)
l = []
for key in d:
   	if d[key] == cont:
   		l.append(key)
l = sorted(l)
print (l)
#rint (l[0])'''


data = ['a', 'g', 'bi', 'bi', 'c']
a = 0
b = 0
cur = data[0]
for i, k in enumerate(data):

    a = data.count(k)

    if b < a:

        b = a
 	
        cur = data[i]
print (cur)
#print(cur)







