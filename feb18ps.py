import datetime
now = datetime.datetime.today()


print('now',now)

def poem():

	print("twinkle,twinkle,little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tlike a diamond in the sky. \nTwinkle,twinkle,little star,\n\t\tlike a diamond in the sky. \nTwinkle,twinkle,little star,\n\tHow I wonder what you are")
	print ("Current date and time: ")

poem()
# print (now.strftime(%Y-%m-%d %H:%M:%S))


# name=input("what is your name?")


def oe():
	x=input("please enter a number")
	print(type(x))
	number=int(x)
	if number%2==0 and number !=0:
		print("the number is even")
	elif number==0:
		print("zero")

	else:
		print("the number is odd")


oe()
