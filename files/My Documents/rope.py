# A rope around the earth at a distance of 1 meter
def circumference(radius):
    return 2* 3.14159 * radius

def radius(circumference):
    return circumference / 2 / 3.14159

earth_circ = 40000 * 1000 # meters
earth_radius = radius(earth_circ)
rope_radius = earth_radius + 1
rope_circ = circumference(rope_radius)
print(rope_circ)

