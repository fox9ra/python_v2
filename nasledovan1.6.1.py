setclass = {}

def add_class(setclass, name_class, parrent):
	if name_class not in setclass:
		setclass[name_class] = []
	setclass[name_class].extend(parrent)
	for i in parrent:
		if i not in setclass:
			setclass[i] = []

def found(setclass, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in setclass:
		return None
	for node in setclass[start]:
		if node not in path:
			newpath = found(setclass, node, end, path)
			if newpath: return newpath
	return None

def answer(setclass, parrent, child):
	if not(parrent or child) in setclass or not found(setclass, child, parrent):
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
    inputdata = input().split()
    parent = inputdata[0]
    child = inputdata[1]
    print(answer(setclass, parent, child))

#print(setclass)

'''
#good from stepik 1
n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")

#good from stepik 2
def find_path(start, path):
    path.add(start)
    for node in graph[start]:
        if node not in path:
            find_path(node, path)

graph = {}
for i in range(int(input())):
    s = input().split()
    graph[s[0]] = s[2:] if len(s) > 1 else [s[0]]

for i in range(int(input())):
    s = input().split()
    path = set()
    find_path(s[1], path)
    print('Yes' if s[0] in path else 'No')

'''