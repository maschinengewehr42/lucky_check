import sqlite3

conn=sqlite3.connect('lucky.sqlite3')
c=conn.cursor()

percent=list()
total=0

for x in range(0, 28):
	c.execute("SELECT lucky1 FROM lucky WHERE lucky1=='%s';"%(x))
	new=c.fetchall()
	an=100*len(new)/1000000
	print("+------------------------------------------+")
	print("|АНАЛИЗ")
	print("|сумма: ",x)
	print("|вероятность выпадения билета: ", str(an)+"%")
	print("|количестко комбинаций для получения: ", len(new))
	print("+------------------------------------------+")
	print()
	percent.append(an)

for x in range(len(percent)):total+=percent[x]

print()
print("+------------------------------------------+")
print("|общая вероятность: ",str(total)+"%")
print("+------------------------------------------+")

c.close(), conn.close()