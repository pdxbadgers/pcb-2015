#!/usr/bin/python

from xml.dom.minidom import parse, parseString
import sys
import numpy as np


def transform_coordinates(x, y, scale, x_translate, y_translate):
    xfrom = np.matrix("%f 0 %f; 0 %f %f; 0 0 1" % (scale, x_translate, -scale, y_translate))
    input_matrix = np.matrix([[x], [y], [1]])
    out = xfrom * input_matrix
    return (out.item(0), out.item(1))

if len(sys.argv) < 6:
    print "usage: ./script.py <input filename> <output filename> <scale> <x_translate> <y_translate>"
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
scale_factor = float(sys.argv[3])
x_trans = float(sys.argv[4])
y_trans = float(sys.argv[5])

min_x = 1000
max_x = -1000
min_y = 1000
max_y = -1000
TARGET_SPAN = 3.550

with open(output_file, "w") as f:
    f.write("LAYER 20;\n");
    f.write("GRID FINEST;\n");
    f.write("SET WIRE_BEND 2;\n");

    dom = parse(sys.argv[1])
    for node in dom.getElementsByTagName('polygon'):
        point_str = node.attributes[u'points'].value
        points = []
        for pair in point_str.split(' '):
            strcoords = pair.split(',')
            (x, y) = transform_coordinates(float(strcoords[0]),
                                           float(strcoords[1]),
                                           scale_factor,
                                           x_trans,
                                           y_trans)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            points.append((x,y))
        f.write("WIRE ")
        for point in points:
            f.write("(%f %f) " % point)
        f.write(";\n")

    f.write("GRID DEFAULT;\n");

print "min x:", min_x
print "max x:", max_x
print "min y:", min_y
print "max y:", max_y

print "x,y translate: %f,%f" % (x_trans, y_trans)
print "scale factor:", scale_factor
print "lower left corner: %f, %f" % (min_x, min_y)
print "upper right corner: %f, %f" % (max_x, max_y)
width = (max_x - min_x)
height = (max_y - min_y)
print "width x height: %f (%02.1f cm) x %f (%02.1f cm)" % (width, width*2.54, height, height*2.54)
center_x = (max_x + min_x)/2.0
center_y = (max_y + min_y)/2.0
print "center: %f,%f" % (center_x, center_y)
