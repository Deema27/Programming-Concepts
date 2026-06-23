''' Description:
Prompts the user for the number of sides and side lengths
of a polygon, then calculates and displays the polygon's
perimeter and area. '''

import math


class Polygon:

    #Constructor initializes default values
    def __init__(self):
        self.__num_sides = 0
        self.__side_length = 0.0

    #Sets the number of sides
    def set_num_sides(self, n):
        self.__num_sides = n

    #Sets the side length
    def set_side_length(self, length):
        self.__side_length = length

    #Returns the number of sides
    def access_num_sides(self):
        return self.__num_sides

    #Returns the side length
    def access_side_length(self):
        return self.__side_length

    #Calculates and returns the perimeter
    def calculate_perimeter(self):
        return self.__num_sides * self.__side_length

    #Calculates and returns the area of a regular polygon
    def calculate_area(self):
        return (self.__num_sides * self.__side_length ** 2) / (
            4 * math.tan(math.pi / self.__num_sides)
        )


def main():

    #Create a Polygon object
    polygon = Polygon()

    #Ask user for number of sides
    num_sides = int(input("Enter the number of sides (>=3): "))

    #Validate that the polygon has at least 3 sides
    while num_sides < 3:
        num_sides = int(input("Invalid entry. Re-enter the number of sides (>=3): "))

    #Ask user for side length
    side_length = float(input("Enter the length of each side (>= 0.1): "))

    #Validate that the side length is at least 0.1
    while side_length < 0.1:
        side_length = float(input("Invalid entry. Re-enter the length of each side (>= 0.1): "))

    #Store user input in the Polygon object
    polygon.set_num_sides(num_sides)
    polygon.set_side_length(side_length)

    #Display polygon information
    print(f"The polygon has {polygon.access_num_sides()} sides. "
          f"Each side is {polygon.access_side_length()} units in length.")

    #Calculate perimeter and area
    perimeter = polygon.calculate_perimeter()
    area = polygon.calculate_area()

    #Display perimeter and area
    print(f"The perimeter of the polygon is {perimeter:.3f} units "
          f"and its area is {area:.3f} square units.")


#Call the main function
main()
