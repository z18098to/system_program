def fb(n):
	if n%3 == 0 and n%5 ==0:
		ret="FizzBuzz"
	elif n%3 == 0:
		ret="Fizz"
	elif n%5 ==0 :
		ret="Buzz"
	else:
		ret="--"
	return ret

i=1
while i<=20:
	print(i,fb(i))
	i=i+1