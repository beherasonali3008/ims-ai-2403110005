import cadquery as cq

# Day 8: Create a 2x4 toy brick with 8 studs
length = 31.2
width = 15.6
height = 9.6

stud_d = 4.8
stud_h = 1.7
spacing = 7.8

brick = cq.Workplane("XY").box(length, width, height)

# Add 4 columns x 2 rows of studs
for i in range(4):
    for j in range(2):
        x = (i - 1.5) * spacing
        y = (j - 0.5) * spacing

        stud = (
            cq.Workplane("XY")
            .workplane(offset=height / 2)
            .center(x, y)
            .circle(stud_d / 2)
            .extrude(stud_h)
        )

        brick = brick.union(stud)

print("Valid solid:", brick.val().isValid())
print("Volume:", round(brick.val().Volume(), 1))

brick.val().exportStl("brick.stl")
