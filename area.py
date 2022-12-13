import numpy as np

def area_circle(radius = 2, n_points = 500000):
    in_circle = 0

    for i in range(0, n_points):
        x = np.random.uniform(-radius, radius)
        y = np.random.uniform(-radius, radius)
        if x**2 + y**2 < radius**2:
            in_circle += 1

    area = (2*radius)**2 * in_circle/n_points
    return area


if __name__ == '__main__':
	n_points = 50000
	radius = 2
	area = area_circle(radius, n_points)
	expected_area = np.pi*radius**2
	print('The area of the circle is {}, expected result {}, difference: {}'.format(area, expected_area, np.abs(area - expected_area)))


