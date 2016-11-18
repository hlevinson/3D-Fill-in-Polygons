import re, os

data = {}

with open('seg_file.txt', 'r') as in_file:
    s = in_file.read()
    objects = re.finditer(r'Object: (?P<object>[a-z0-9]+).*?(?:\s+Plane Number:\s([0-9]+)\n\n\s+Traces:\s[0-9]+\n\n\s+Trace:\s[0-9]+\n\s+Number Points: [0-9]+\n(?:\s+[0-9.]+ [0-9.]+\n)+\n)+',
                          s , re.DOTALL)
    for o in objects:
        obj = o.group(1)
        data[obj] = {}
        planes = re.finditer('(?:\s+Plane Number:\s(?P<plane_number>[0-9]+)\n\n\s+Traces:\s[0-9]+\n\n\s+Trace:\s[0-9]+\n\s+Number Points: [0-9]+\n(?:\s+[0-9.]+ [0-9.]+\n)+\n)',
                             o.group(0), re.DOTALL)
        for p in planes:
            z = p.group(1)
            data[obj][z] = []
            points = re.finditer('(?P<point>\s+[0-9.]+ [0-9.]+\n)', p.group(0), re.DOTALL)
            for pt in points:
                str_pt = pt.group(1).split(' ')
                data[obj][z].append((float(str_pt[0]), float(str_pt[1])))


for obj in data.keys():
    try:
        os.makedirs(os.path.join('parsed_data', obj))
    except:
        print '{} exists!'. format(os.path.join('parsed_data', obj))
    for z in data[obj].keys():
        with open(os.path.join('parsed_data', obj, z+'.dat'), 'w') as out_file:
            for pt in data[obj][z]:
                x, y = pt
                out_file.write('{},{},{}\n'.format(x, y, z))
