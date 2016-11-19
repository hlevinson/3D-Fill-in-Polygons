import re, os
import numpy as np
import cPickle as pickle

data = {}
with open('seg_file.txt', 'r') as in_file:
    s = in_file.read()
    # Parses out object chunks
    objects = re.finditer((r'Object: (?P<object>[a-z0-9]+).*?'
                            '(\s+Plane Number: ([0-9]+)\n\n\s+Traces: [0-9]\n\n'
                            '(\s+Trace: [0-9]+\n\s+Number Points: [0-9]+\n'
                            '(\s+[+-]?[\d.]+ [+-]?[\d.]+\n)+\n)+)+'),
                          s , re.DOTALL)
    plane_count = 0
    for o in objects:
        color = np.random.rand(1,3)[0]
        o_name = o.group(1)
        data[o_name] = {}
        # parses out planes from objects
        planes = re.finditer(('\s+Plane Number:\s(?P<plane_number>[0-9]+)\n\n\s+Traces:\s[0-9]+\n\n'
                              '(\s+Trace: [0-9]+\n\s+Number Points: [0-9]+\n'
                              '(\s+[+-]?[\d.]+ [+-]?[\d.]+\n)+\n)+'),
                             o.group(0), re.DOTALL)
        for p in planes:
            p_name = p.group(1)
            data[o_name][p_name] = []
            traces = re.finditer(('\s+Trace:\s[0-9]+\n\s+Number Points: [0-9]+\n'
                                  '(?:\s+[+-]?[\d.]+ [+-]?[\d.]+\n)+'),
                                 p.group(0), re.DOTALL)
            for t in traces:
                # parses out points in each plane
                t_list = []
                points = re.finditer('(?P<point>\s+[+-]?[\d.]+ [+-]?[\d.]+\n)',
                                     t.group(0), re.DOTALL)
                for pt in points:
                    str_pt = pt.group(1).split(' ')
                    t_list.append([float(str_pt[0]), float(str_pt[1]), float(p_name), color[0] , color[1], color[2]])
                data[o_name][p_name].append(t_list)

# Dump data to different files
for o in data.keys():
    try:
        os.makedirs(os.path.join('parsed_data', o))
    except:
        print '{} exists!'. format(os.path.join('parsed_data', o))
    for p in data[o].keys():
        i = 0
        for t in data[o][p]:
            with open(os.path.join('parsed_data', o, '{}_{}.dat'.format(p,i)), 'w') as out_file:
                for pt in t:
                    x, y, z, r, g, b = pt
                    out_file.write('{},{},{},{},{},{}\n'.format(x, y, z, r, g, b))
            i+=1

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
