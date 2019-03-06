n=int(input())
dic = {'global': {'parent': 'None', 'vars': []}}

def create(namespace, parent):
	if namespace not in dic:
		dic[namespace] = {'parent': parent, 'vars':[] }

def add(namespace, var):
	dic[namespace]['vars'].append(var)

def get(namespace,var):
	if namespace in dic:
		if var in dic[namespace]['vars']:
			print ("test1:",namespace)
			return namespace
		elif dic[namespace]['parent'] == "None":
			print("test2:",namespace)
			if var in dic['global']['vars']:
				return "global"
			else:
				return "None"
		else:
			get(dic[namespace]['parent'],var)

				

for i in range(n):
	#print(n)
	cmd, nmsp, var = input().split()
	if cmd == "create":
		create(nmsp,var)
	elif cmd == "add":
		add(nmsp,var)
	elif cmd == "get":
		print(get(nmsp,var))

print(dic)