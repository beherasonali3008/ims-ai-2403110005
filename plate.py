import cadquery as cq

# Day 7: Create a rectangular plate with a cylindrical hole
plate = cq.Workplane("XY").box(80, 50, 10)
hole = cq.Workplane("XY").cylinder(10, 10)

part = plate.cut(hole)

print("Valid solid:", part.val().isValid())
print("Volume:", round(part.val().Volume(), 1))

cq.exporters.export(part, "plate.stl")
