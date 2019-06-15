def reverse(s):
	ret=""
	for i in range(0,len(s)):
		ret=ret+s[-(i+1)]

	if s==ret:
		ret="** palindrome **"

	return ret

orig=input("Type a phrease:")
result=reverse(orig)
print(result)


