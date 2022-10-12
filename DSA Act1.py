from math import pi

choose = input("Radius or Diameter: ").capitalize()

class Radius:
  def __init__(self,radius):
    self.radius = radius

  def area(self):
    return pi * (int(self.radius) ** 2)

  def display(self):
    print("The area of the circle is",  round(self.area(),2))

class Diameter:
  def __init__(self,diameter):
    self.diameter = diameter

  def area(self):
    return pi * (int(self.diameter) ** 2)/4

  def display(self):
    print("The area of the circle is", round(self.area(),2))


if choose == "Radius":
  R = Radius(int(input("Radius: ")))
  R.display()

if choose == "Diameter":
  D = Diameter(int(input("Diameter: ")))
  D.display()

if choose != "Diameter" and choose != "Radius":
  print("error")