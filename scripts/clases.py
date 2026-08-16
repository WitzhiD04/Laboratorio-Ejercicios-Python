import matplotlib.pyplot as plt
import matplotlib.patches as patches

#plt.show()

class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

class Rectangulo(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


RedCircle = Circle(10, 'red')
print(RedCircle.radius)
print(RedCircle.color)
print('\n')

RedCircle.radius = 1

RedCircle.drawCircle()

RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

BlueCircle = Circle(radius=100)

BlueCircle.drawCircle()

SkinnyBlueRectangle = Rectangulo(2, 10, 'blue')
SkinnyBlueRectangle.drawRectangle()

FatYellowRectangle = Rectangulo(20, 5, 'yellow')
FatYellowRectangle.drawRectangle()

print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

class Ellipse(object):

    # Constructor
    def __init__(self, width, height, color1='r', color2='b'):
        self.height = height
        self.width = width
        self.color1 = color1
        self.color2 = color2
        self.xy = (0,0)
    
    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setcolor1(self, color1):
        self.color1 = color1
    
    def setcolor2(self, color2):
        self.color2 = color2

    # Method
    def drawEllipse(self):
        plt.gca().add_patch(patches.Ellipse(self.xy, width = self.width, height = self.height, facecolor = self.color1, edgecolor = self.color2))
        plt.axis('scaled')
        plt.show()


ellipse = Ellipse(1, 2, 'red', 'blue')
ellipse.drawEllipse()

ellipse.setHeight(20)
ellipse.setWidth(45)
ellipse.setcolor1('yellow')
ellipse.setcolor2('green')
ellipse.drawEllipse()