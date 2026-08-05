from shapes.two_d import circle
from shapes.three_d.sphere import volume

print(circle.area(3))
print(volume(3))

# Or:
import shapes
print(shapes.two_d.circle.area(3))
print(shapes.three_d.sphere.volume(3))