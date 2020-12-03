# create a function that checks if the number is a prime number
def prime_number(num):
  num_divide = num // 2
  num_is_prime = False
  if num == 1:
    return "no"
  elif num == 2:
    return "yes"
  elif num % 2 != 0:
    while num_is_prime == False:
      for i in range(num_divide, 0, -1):
        if i == 1:
          num_is_prime = True
        elif num % i == 0:
          return "no"
        else:
          num_is_prime = False
    return "yes"
  else:
    return "no"

# Print a list of numbers and whether each number in the list is a prime or not
print("----------List of numbers and whether they are prime or not--------")
# get user input for the length of the list
prime_number_range = int(input("Up to what number would you like to check for prime's? "))
# return whether each number in the list is a prime or not
for i in range(prime_number_range+1):
    print(i, prime_number(i))

# Check if a number is prime
print("---------A number and if it is prime ---------")
# Get user input for which number to check
prime_number_check = int(input("What number would you like to check whether or not it is a prime? "))
# return whether the number is a prime or not
print(prime_number_check, prime_number(prime_number_check))

# ----------------------------------------------------
# Create a function that finds the nth prime number
def nth_prime_number(n):
  # counter for which prime number it is at
  prime_number_counter = 0

  # Counter for the current number testing if it is a primenumber
  current_number = 0

  # Check whether we have found the nth prime
  found_n = False

  while found_n == False:
    # check if the number is prime
    prime_check = prime_number(current_number)

    # if it is not, check the next number
    if prime_check == "no":
      current_number += 1
    # if it is, add 1 to our prime number counter
    elif prime_check == "yes":
      prime_number_counter += 1
        # if the prime number is the nth prime number, we found n
      if prime_number_counter == int(n):
        found_n = True
      # otherwise, continue with the next number
      else:
        current_number += 1
  # when we find the nth prime number, return which number that is
  return current_number

# find the nth prime number
print("-------------The nth prime number-------------")
# Get user input on which nth prime number to find
nth_prime = input("Which nth prime number would you like to know? ")
# Print the nth number and which prime number it is
if nth_prime[-1] == "1":
    print(f"The {nth_prime}st prime number is  {nth_prime_number(nth_prime)}")
elif nth_prime[-1] == "2":
    print(f"The {nth_prime}nd prime number is  {nth_prime_number(nth_prime)}")
elif nth_prime[-1] == "3":
    print(f"The {nth_prime}rd prime number is  {nth_prime_number(nth_prime)}")
else:
    print(f"The {nth_prime}th prime number is  {nth_prime_number(nth_prime)}")


# print("8th", nth_prime_number(8))


# --------------------------------------------------------------
# Create a function to find what power of 2 a number is
def power_of_2(root):
    power = 0
    new_num = root
    power_of_two = False
    while power_of_two == False:
        if new_num % 2 == 0:
            new_num = new_num / 2
            power += 1
            if 2 ** power == root:
                power_of_two = True
            else:
                power_of_two = False
        else:
            return False
    return power_of_two

# return a list of numbers and if each number is a power of two
print("-----------A list of numbers and whether it is a power of 2----------------")
# get user input for the length of the list
power_of_2_len = int(input("Up to what number do you want to check for power's of 2? "))
# print the number and whether it is a power of 2
for i in range(1, power_of_2_len + 1):
    if power_of_2(i) == True:
        print(i, "yes")
    else:
        print(i, "no")


# Create a function that checks if a number is a Mersenne Prime
def mersenne_prime(mersenne_num):
    if prime_number(mersenne_num) == "yes":
        return (power_of_2(mersenne_num + 1))
    else:
        return False

# check whether a number is a Mersenne Prime
print("-----------A number and whether it is a Mersenne Prime-------------")
# get user input for which number to check
mersenne_prime_check = int(input("What number do you want to for being a Mersenne prime? "))
# print if the number is a mersenne prime
if mersenne_prime(mersenne_prime_check) == True:
    print(mersenne_prime_check, "yes")
else:
    print(mersenne_prime_check, "no")
