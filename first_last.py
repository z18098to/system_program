def first_last(s):
	if len(s)>1:
		ret= s[:2]+s[-2:]
	else:
		ret= ""
	return ret

print(first_last("spring"))
print(first_last("hello"))
print(first_last("a"))
print(first_last("abc"))
