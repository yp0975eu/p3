class Menu():
    """
    stores options in datastructures for easy retreival
    """
    def __init__(self):
        self.options = {}
        self.text = {}
        self.functions = {}

    def add(self, key, text, function):
        self.text[key] = text
        self.functions[key] = function

    def show(self):
      print()
      for key in self.text.keys():
          print(f"{key}: {self.text[key]}")

    def get(self, key):
      if key in self.text.keys():
          return self.functions[key]
      else:
          print(f"option \"{key}\" doesn't exist")
          return False
