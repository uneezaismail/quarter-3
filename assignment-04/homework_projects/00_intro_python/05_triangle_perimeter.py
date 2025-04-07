# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).


def triangle_perimeter():
    triangle_base = float(input("Enter the length of the base of the triangle: "))
    triangle_height = float(input("Enter the length of the height of the triangle: "))
    triangle_hypotenuse = float(input("Enter the length of the ypotenuse of the triangle: "))

    perimeter_of_triangle = triangle_base + triangle_height + triangle_hypotenuse

    print(f"\nThe perimeter of the triangle is : {perimeter_of_triangle}")


triangle_perimeter()    