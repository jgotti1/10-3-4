class Dog:
    def __init__(self, x, y):
      self.name= x
      self.age= y
  

    def get_name(self):
      return self.name
      
    def get_age(self):
      return self.age
   
d = Dog("Timmy")
d2 = Dog("Billy")
print (d.get_name())
print (d2.get_name())

