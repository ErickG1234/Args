# Args means I can use as many arguments as possible (limitless arguements)
# def sun(num1, num2):
#   return num1 + num2

# print(sum(2,3))  wont work: too many arguments

def sum(*args):
  total = 0 
  for arg in args:
    total += arg
  return total

print(sum(2,3,4,55,6,88,445,66,23))

# kwargs means using key values(limitless)
# its a step beyond args 
def a_sum(**kwargs): #Use two asterisks = keys and values
  total = 0 
  for key, value in kwargs.items():
    print(f'{key} = {value}')
    total += value
  return total

print(a_sum(x = 3,y = 5, z = 22))