
pad_height = 1.5
pad_width = 0.7

def smd(f, x):
    pad_height = 1.5
    pad_width = 0.7
    y = 1.0  + pad_height/2 # pads are 1.0 above 0
    f.write("SMD %f %f (%f %f);\n" % (pad_width, pad_height,
                                        x, y))

with open("switch.scr", "w") as f:
    f.write("GRID MM;\n")
    # make the holes
    f.write("HOLE 0.9 (-1.5 0);\n")
    f.write("HOLE 0.9 (1.5 0);\n")

    # pin2 center line is 0.75 to the right of 0
    smd(f, 0.75)

    # pin3 center line is 1.5 to the right of 0.75
    smd(f, 1.5 + 0.75)
    
    # pin1 centerline is 2 to the left of pin3
    smd(f, 0.75 - 3.0)
