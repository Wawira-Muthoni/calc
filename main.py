from email.errors import NoBoundaryInMultipartDefect
from nis import cat
from urllib.request import HTTPPasswordMgrWithPriorAuth


name = "Emeka"
age = 35
pet  = cat
city = "Hawii"
#Ask the name of the person
person_name =input("What is your name?\n")

#Ask the age
age_int=input("What is your age?\n")
#Ask the favourite pet
pet_name =input("What is your favourite pet?\n")
#Ask the name of city the person grew up in.
city_name = input("What is the name of city you grew up in?\n")
#Combine the name,age, pet and city name
print("I am " + name + "and I am " +age+ "I love  " +pet+ "and I am from" +city)