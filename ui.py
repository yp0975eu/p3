
def get_price():
  """
  gets a integer grater than 0 and less than 1 million
  """
  min = 0
  max = 1000000
  question = "Enter a price: "
  while True:
    try:
      price = int(input(question))
      if (price > min and price < max):
        return price
      else:
        print(f'Please enter a value greater than {min} and less than {max}')
    except ValueError:
      print('Please enter a number')

def get_string(question):
  """
  returns any string with at least one character
  """
  while True:
    name = input(question)
    if (len(name) > 0):
      return name
    else:
      print(f'Please enter at least character')

def get_positive_integer(question):

  while True:
    number = int(input(question))
    if (number > 0):
      return number
    else:
      print(f'Please enter a positive number ')

def get_string_from_options(question, options):
  """
  returns an answer from a set of optionss
  """
  while True:
    answer = input(question)
    if (answer.lower() in options):
      return answer
    else:
      print(f'Please enter a valid answer ')

def display(message):
  print()
  print(message)
