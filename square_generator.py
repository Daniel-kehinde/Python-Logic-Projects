# Square Calculator Tool
# Built by Daniel Kehinde

num = int(input('Enter a number: '))
num1 = int(input('Enter where it should stop: '))

print("-" * 24)

# We use num1 + 1 so the loop actually hits the user's last number
for x in range(num, num1 + 1):
    answer = x ** 2
    # Clean, professional output formatting
    print(f"{x} square is {answer}")

print("-" * 24)
print("Calculation Finished!")
	