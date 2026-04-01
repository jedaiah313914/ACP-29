data = ["Codingal", 3, "is", 2, "best", 2, "for", 2, "Coding", 1]

print("The list is:", data)

value_input = input("Enter the value you want to check the frequency of: ")

try:
    value = int(value_input)
except ValueError:
    value = value_input

frequency = data.count(value)

print(f"The frequency of {value} is {frequency}")
