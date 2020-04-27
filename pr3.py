less_specific = 5

def foo():
	more_specific = 2
	print("Inside foo:", less_specific)
	
foo()
print(more_specific)