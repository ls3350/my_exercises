def dish():
	costofmeal=int(input("cost of meal"))
	costoftip=0.18
	costoftax=0.09
	tipamount=costofmeal*costoftip
	taxamount=costofmeal*costoftax
	totalamount=costofmeal+tipamount+taxamount
	print "Total of the meal is $", totalamount
dish()