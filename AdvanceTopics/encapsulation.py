class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def return_width(self):
        return self.width

    def return_length(self):
        return self.length

    def change_width(self, w):
        self.width = w

    def change_length(self, l):  
        self.length = l

    def area(self):
        return self.width * self.length


class Data:
    def __init__(self):
        self.number_list = [x for x in range(1, 10) if x % 2 != 0]

    def change_data(self, index, n):
        if 0 <= index < len(self.number_list):
            self.number_list[index] = n
        else:
            print("Error: Index out of range.")

    def add_number(self, n):
        self.number_list.append(n)

    def remove_number(self, n):
        if n in self.number_list:
            self.number_list.remove(n)
        else:
            print(f"{n} not found in the list.")

    def display_data(self):
        print(self.number_list)

    def sum_data(self):
        return sum(self.number_list)

    def average_data(self):
        if len(self.number_list) == 0:
            return 0
        else:
            return sum(self.number_list) / len(self.number_list)


rectangle = Rectangle(5, 10)

# methods of Rectangle
print("Rectangle Width:", rectangle.return_width())
print("Rectangle Length:", rectangle.return_length())
print("Rectangle Area:", rectangle.area())


data = Data()
data.display_data()
print("Sum of Data:", data.sum_data())
print("Average of Data:", data.average_data())

data.change_data(2, 15)
data.display_data()
print("Sum of Modified Data:", data.sum_data())
print("Average of Modified Data:", data.average_data())
