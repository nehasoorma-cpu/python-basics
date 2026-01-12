# -----------------------------
# PYTHON BASICS PRACTICE FILE
# -----------------------------

# 1. Variables & Data Types
name = "Neha"
birth_year = 1985
city = "Indore"
is_learning = True

print("Name:", name)
print("City:", city)
print("Learning Python:", is_learning)

# 2. Calculations
current_year = 2026
age = current_year - birth_year
print("Age:", age)

# 3. Decision Making
if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")

# 4. Loops
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(i)

# 5. Even / Odd Check
print("\nEven or Odd Check:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

# 6. Functions
def greet_user(name):
    return f"Hello, {name}!"

print("\nFunction Output:")
print(greet_user("Neha"))

def calculate_age(birth_year):
    return current_year - birth_year

print("Calculated Age:", calculate_age(1985))

def is_even(number):
    return number % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))

