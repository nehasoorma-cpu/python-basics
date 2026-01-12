print("Hello, Python!")

age = 41

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
for i in range(1, 6):
    print("Number:", i)
count = 1

while count <= 5:
    print("Count:", count)
    count += 1
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
def greet():
    print("Hello from a function")

greet()
greet()
def calculate_age(birth_year):
    current_year = 2026
    return current_year - birth_year

age = calculate_age(1985)
print("Calculated age:", age)
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(7))
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(9))
