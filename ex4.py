# the variable cars = 100
cars = 100

#the variable space_in_a_car equals 4
space_in_a_car = 4

# the variable drivers equals 30
drivers = 30

# the variable drivers equals 90
passengers = 90

#the value of cars_not_driven is equal to cars(100) - drivers(30)
cars_not_driven = cars - drivers

#cars_driven is equal to the value of drivers, which is 30.
cars_driven = drivers

#carpool_capacity is equal to the value of cars_driven(30) multiplied by the value of space_in_a_car (4)
carpool_capacity = cars_driven * space_in_a_car

#average_passengers_per_car is equal to the value of passengers (90) / the value of cars_driven (30)
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "there are only", drivers, "drivers available"
print "There will be ", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# the decimal point dropped off of 120.
