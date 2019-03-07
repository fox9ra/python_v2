#ex1.4.1 пример работы и поиска пространсва имен с использованием словарей

n=int(input())
dic = {'global': {'parent': 'None', 'vars': []}}

def create(namespace, parent):
	if namespace not in dic:
		dic[namespace] = {'parent': parent, 'vars':[] }

def add(namespace, var):
	dic[namespace]['vars'].append(var)

def get(namespace,var):
	if namespace in dic:
		#print("test0:",namespace)
		#print("test0.1",dic[namespace]['parent'])

		if var in dic[namespace]['vars']:
			#print ("test1:",namespace)
			return namespace
		elif dic[namespace]['parent'] == "global":
			#print("test2:",namespace)
			if var in dic['global']['vars']:
				return "global"
			else:
				return "None"
		else:
			return(get(dic[namespace]['parent'],var))
				

for i in range(n):
	#print(n)
	cmd, nmsp, var = input().split()
	if cmd == "create":
		create(nmsp,var)
	elif cmd == "add":
		add(nmsp,var)
	elif cmd == "get":
		#print ("incoming:", nmsp, var)
		print(get(nmsp,var))

#print(dic)

'''
#good stepic
dct={'global':['None']}                                             # словарь списков(родитель,переменные)
for ops, nms, v in [input().split() for i in range(int(input()))]:  # цикл операций(копипаст у Vladmir Ryabov)
    if   ops=='create':dct[nms]=[v]                                 # создать пространство-новый список в словаре
    elif ops=='add'   :dct[nms].append(v)                           # новая переменная-добавить в список
    elif ops=='get':                                                # поиск переменной (циклом)
        while nms!='None' and v not in dct[nms]:                    # если нет в пространстве-меняем на родителя(пока не None)
            nms=dct[nms][0]                     
        print(nms)
'''