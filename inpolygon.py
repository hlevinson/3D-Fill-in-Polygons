import pandas
from shapely.geometry import Polygon

points = pandas.read_csv('parsed_data/b1/153.dat', names=['x','y','z']).as_matrix()
poly = Polygon(points)

