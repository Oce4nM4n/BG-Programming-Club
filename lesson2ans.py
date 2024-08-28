def answer(question:int)->str:
	match question:
		case 1:
			reply="Dictionary has keys which correspond to values, while a list is just a list of things which you can index"
		case 2:
			reply="sets are immutable objects with no order while tuples are just immutable lists"'
		case 3:
			reply="() or tuple()"
		case 4:
			def triangle(height:int)->None:
				for i in range(0, height+1):
					for squares in range(0, i+1):
						print("#", end="")
				print("")
			triangle(5)

		case 5:
			class House():
				def __init__(self, size, bedrooms, bathrooms):
					self.size=size
					self.bedrooms=bedrooms
					self.bathrooms=bathrooms

				def sell(self):
					self.price = self.size*230+(self.bedrooms*32*self.bathrooms*434)#this is an absolutely random formula
					print(f"you sold the house for ${self.price}")

	return reply
