def ifstatements():

	weather=str(input("type of weather"))
	if weather=="rain":
		print("please take umbrella")

	elif weather=="sunny":
		print("please take sun glasses")
	elif weather=="snow":
		print("please take coat")
	else:
		print("it is not a valid answer")
ifstatements()