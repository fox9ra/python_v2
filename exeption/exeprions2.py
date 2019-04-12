setclass = {}

def add_class(setclass, name_class, parrent):
	if name_class not in setclass:
		setclass[name_class] = []
	setclass[name_class].extend(parrent)
	for i in parrent:
		if i not in setclass:
			setclass[i] = []
	print (setclass)

def found(setclass, start, path=[]):
	path = path + [start]
	print(setclass, "=", start, "=", path)
	if start not in setclass:
		return None
	for node in setclass[start]:
		if node not in path:
			newpath = found(setclass, node, path)
			if newpath: return newpath
	return None

def answer(setclass, parrent):
	if not(er) in setclass or not found(setclass, er):
		return 'No'
	return 'Yes'

n = int(input())
for i in range(n):
    inputdata = input().split()
    parents = []
    name = inputdata[0]
    parents = inputdata[2:]
    #print("name=", name, "parents=", parents)
    add_class(setclass, name, parents)

q = int(input())
for i in range(q):
    er = input()
    print(answer(setclass, er))

#print(setclass)