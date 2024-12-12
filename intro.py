name = "Angel"
age = 25
height = 6.0
is_student = True
name = True
name = 123
print (f"Name: {name}, age: {age}, height: {height}")
print ("Type of age: ", type(name))

age = 25
if age < 13:
    print ("Child")
elif age < 20:
    print ("Teenager")
else: 
    print ("Adult")

# for loops
for numbers in range(5):
    print(numbers)

# List --> array
fruits = ["Apple", "banana", "cherry"]
print(fruits)
fruits.append("date")
print(fruits)
print (fruits[1:3])

# dictionary
student = {
    "name": "Adrian",
    "age": 20,
    "cousers": ["math", "sciences"]
}
print(student["age"])
student["grade"] = "A"
student.update({"email":"angelvalentin@gmail.com"})
print(student)

# functions
def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")

#call the functions 
say_hello()
say_goodbye()

# concatenate
print("Hello my name is " + name + " and i have" + str(age) + "old")

