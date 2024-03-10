class Circle:
    def __init__(self, data):
        self.data = data
        self.__pi = 3.141  # Private member variable

    def calculate_area(self, radius):
        area = self.__pi * radius * radius
        return area

    def calculate_perimeter(self, radius):
        perimeter = 2 * self.__pi * radius
        return perimeter

# Radius input as a list
data_list = [10, 501, 22, 37, 100, 999, 87, 351]
#Creating a circle object with given data.
circle = Circle(data_list)


for radius in data_list: # Calculate and print area and perimeter for each radius in the data list
    area = circle.calculate_area(radius)
    perimeter = circle.calculate_perimeter(radius)
    print(f"Radius: {radius}, Area: {area}, Perimeter: {perimeter}")
