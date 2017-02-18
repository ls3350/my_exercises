def tryrange():
	list_of_items=["bread","cheese","oil","apple","rice"]

	cart = []

	x = len(list_of_items)

	while x > 0:
		x = x - 1
		print(x)
		for item in list_of_items:
			if item not in cart:
				cart.append(item)
			

	print("my cart",cart)


tryrange()