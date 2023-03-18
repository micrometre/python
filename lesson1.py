def printPerimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    #print(perimeter)
    return perimeter
#printPerimeter(10, 11, 4) # => 25


def calculatePerimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    print(perimeter)
    return perimeter

perimeter1 = calculatePerimeter(6, 4, 3)
perimeter2 = calculatePerimeter(10, 3, 11)

print("The perimeter of my first triangle is", perimeter1, "and that of my second is", perimeter2)    