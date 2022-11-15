# Erick , Arturo , Camelot

# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


def sum_squares(*args):
  total = 0
  for arg in args:
    total += arg
  return total




########################################################################################################################
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).


def absolute_sum(*args):
  sum = 0
  for arg in args:
    absolute_value = abs(arg)
    sum += absolute_value
  return abs(sum)




########################################################################################################################
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"


def personal_numbers(name, *args):
  sum_numbers = sum(args)
  return f"{name}, the sum of your numbers is {sum_numbers}"
