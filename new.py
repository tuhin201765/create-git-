def triangle(base, hight):
    """
    return area of triangle
    """
    area = 0.5 * base * hight
    return area


def square(length):
    """
    return area of square
    """
    area = length * length
    return area


def rectangle(length, width):
    """
    return area of rectangle
    """
    area = length * width
    return area


print(triangle(2, 3))
print(square(2))
print(rectangle(2, 3))