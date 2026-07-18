def valid_triangle(sides):
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0 and
        a + b >= c and
        a + c >= b and
        b + c >= a
    )
    
def equilateral(sides):
    return valid_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    return valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0])


def scalene(sides):
    return valid_triangle(sides) and (
        sides[0] != sides[1] and
        sides[1] != sides[2] and
        sides[0] != sides[2]
    )
