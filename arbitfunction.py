def my_name(*student):
    print("Hello" + " " + student[2] )

my_name("kim", "alec", "john",)    


def my_country(*country):
    print("you come from " + " " + country[3])


my_country("kenya", "Uganda", "Tanzania", "Egypt")


def my_occupation(*occupation):
    print("You work as" + " " + occupation[-2])

my_occupation("an engineer", "a doctor", "a chef")    

#keyword_functions
 
def my_name(student1, student2, student3):
    print("Hi" + " " + student3) 

my_name(student1="Alex", student2="Kevin", student3="richy" )

def my_country(country1,country2,country3):
    print("You live in" + " " + country2)

my_country(country1 = "Kenya", country2 = "Ethiopia", country3 = "Ghana")



#default functions

def my_colour(colour = "blue"):                             #function without arguement uses the default value
    print("My favorite colour is" + " " + colour)

my_colour("white")    
my_colour("red")
my_colour()
my_colour("orange")

print("Bye bye")
    