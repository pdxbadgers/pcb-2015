#!/usr/bin/python

width = 24
length = 51
pin_spacing = 12.27
pin_diameter = 0.8
pin_centers = pin_spacing - pin_diameter


# pins are in middle of outline
# center is 24/2 - (

output_file = 'battery.scr'

def wire(x1, y1, x2, y2):
    return "WIRE (%f %f) (%f %f);\n" % (x1, y1, x2, y2)

with open(output_file, "w") as f:
    f.write("GRID MM;\n");
    f.write("LAYER 20;\n");
    f.write(wire(0,0, length,0))
    f.write(wire(length,0, length, width))
    f.write(wire(length, width, 0, width))
    f.write(wire(0, width, 0, 0))
    f.write("PAD 0.9 Square (%f %f);\n" % (3, (width/2 - pin_centers/2)))
    f.write("PAD 0.9 Round (%f %f);\n" % (3, (width/2 + pin_centers/2)))
