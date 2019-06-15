def front_back(a,b):
	a1=a[:int(len(a)/2+1/2)]
	a2=a[int(len(a)/2+1/2):]
	b1=b[:int(len(b)/2+1/2)]
	b2=b[int(len(b)/2+1/2):]
	return a1+b1+a2+b2

print(front_back("abcd","xy"))
print(front_back("abcde","xyz"))
print(front_back("Kitten","Donut"))
print(front_back("a","x"))

s1="abcdefghijklmn"
print("")
print(s1[0] + s1[1] + s1[4] + s1[5])
print(s1[0] + s1[1] + s1[-2] + s1[-1])
print(s1[0:2] + s1[-2:-1])
print(s1[0:2] + s1[-2:])
print(s1[:2] + s1[-2])