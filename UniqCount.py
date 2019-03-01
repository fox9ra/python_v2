#ex1.2.1

objects = [1, 2, 1, 2, 3]
ans = 0
n=[]
for obj in objects: # доступная переменная objects
	if obj not in n:
		n.append(obj)
		ans += 1

print(len(n))

'''
# в одну строку
print(len(set(map(id, objects))))
'''