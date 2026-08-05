'''*D3.* Import the 'shapes module using an alias: 'import shapes as sh, and call the functions using the alias.'''

import shapes as sh

side = float(input("Enter the side of square:"))
radius = float(input("Enter the radius of circle:"))
print("The area of square is =",sh.area_square(side))
print("The area of circle is =",sh.area_circle(radius))
