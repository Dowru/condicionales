
def square(length):
    if length > 10:
        area = length ** 2
        return area
    else:
        return "Not applicable"

side = float(input("Enter the side length of the square: "))

result = square(side)
print("Area of the square:", result)
