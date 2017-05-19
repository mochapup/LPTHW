

#Defining variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Cars avilable
print("There are", cars, "cars avilable.")
#Drivers avilable
print("There are only", drivers, "drivers avilable")
#number of empty cars
print("There will be", cars_not_driven, "empty cars today.")
#Capacity for people in carpool
print("We can transport", carpool_capacity, "people today.")
#number of passangers in carpool today
print("We have", passengers, "to carpool today")
#average number of passangers in each car
print("We need to put about", average_passengers_per_car, "in each car.")
