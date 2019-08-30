#program to make a class of house
import matplotlib.pyplot as plt
class House:
	"""docstring for House"""
	def __init__(self, plot,bedrooms,persons,kitchens,bathrooms,halls):
		
		self.plot = plot
		self.bedrooms=bedrooms
		self.persons=persons
		self.kitchens=kitchens
		self.bathrooms=bathrooms
		self.halls=halls

plot=int(input('enter the size of your plot: '))

bedrooms=int(input('how many bedrooms : '))
persons=input('persons that are gonna live ')
kitchens=int(input('kitchen: '))
bathrooms=int(input('bathroom: '))
halls=int(input('halls: '))

#garden is a separate entity
garden=int(input('gardens: '))
#created a object named consumer
consumer=House(plot,bedrooms,persons,kitchens,bathrooms,halls)

print('your house will have ', str(plot) + "sqft  of plot")	

#calculated the whole requirements and divided it into the plot
total= bedrooms+kitchens+bathrooms/2+halls
#we have taken only 60% of the plot to build and rest is for garden and pool
build_up= 0.6 * plot
garden = 0.4 * plot

graph= build_up/total

#Revised vlaues for rooms , no. of room * allotted size out of plot
bedroom = bedrooms * graph
kitchen = kitchens * graph
bathroom = bathrooms * graph
hall = halls * graph


print('the build_ area will be ', str(build_up) + "sqft" + 'for your family of', persons)
print("and this is how the whole segment would look like: ")
 
 #Matplot part

sizes = [bedroom,kitchen,bathroom,hall,garden]

labels = ['bedroom','kitchen','bathroom','hall','garden']

plt.pie(sizes,labels=labels,startangle = 90,autopct='%1.1f%%')
plt.title('Pie chart for whole plot')
plt.show()

