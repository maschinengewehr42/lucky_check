import sqlite3

conn= sqlite3.connect('lucky.sqlite3')
c= conn.cursor()

for x in range(0,1000000):
	num=x
	if num<10:
		new_num=str(num)
		new_num="00000"+new_num
		mod=list(str(new_num))

	elif num <100 and num >= 10:
		new_num=str(num)
		new_num="0000"+new_num
		mod=list(str(new_num))

	elif num <1000 and num >= 100:
		new_num=str(num)
		new_num="000"+new_num
		mod=list(str(new_num))

	elif num <10000 and num >= 1000:
		new_num=str(num)
		new_num="00"+new_num
		mod=list(str(new_num))

	elif num <100000 and num >= 10000:
		new_num=str(num)
		new_num="0"+new_num
		mod=list(str(new_num))

	elif num <1000000 and num >= 100000:
		new_num=str(num)
		new_num=""+new_num
		mod=list(str(new_num))

	mod = [int(i) for i in mod]

	luck1=mod[0]+mod[1]+mod[2]
	luck2=mod[3]+mod[4]+mod[5]
	if luck2 == luck1:
		print(luck1,luck2, mod)
		c.execute("INSERT INTO lucky (lucky1, lucky2, num) VALUES ('%s', '%s', '%s') ;"%(luck1,luck2,mod))
		conn.commit()

c.close(), conn.close()
