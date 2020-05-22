import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks, as long as the program is active.

while True:
	# Make a random walk.
	rw = RandomWalk(5000)
	rw.fill_walk()

    # Plot the points for the simulated grain of pollen.
	plt.style.use('classic')
	fig, ax = plt.subplots()
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=1)

	plt.show()
