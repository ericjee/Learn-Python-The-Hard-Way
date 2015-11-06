# -*- coding: utf-8 -*-
# 车辆数
cars = 100
# 座位数
space_in_a_car = 4.0
# 司机人数
drivers = 30
# 乘客人数
passengers = 90
# 空闲的车辆数
cars_not_driven = cars - drivers
# 有司机驾驶的车辆数
cars_driven = drivers
# 载客数
carpool_capacity = cars_driven * space_in_a_car
# 平均车载乘客数
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
