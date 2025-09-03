from drunk import TraditionalDrunk
from field import Field
from coordinates import Coordinates
from bokeh.plotting import figure, show


def hike(field, drunk, steps):
    start = field.get_coordinate(drunk)

    for _ in range(steps):
        field.move_drunk(drunk)
    
    return start.distance(field.get_coordinate(drunk))


def walk_simulator(steps, attempts_number, kind_of_drunk):
    drunk = kind_of_drunk(name='Jim')
    origin = Coordinates(0, 0)
    distances = []
    
    for _ in range(attempts_number):
        field = Field()
        field.add_drunk(drunk, origin)
        walk_simulation = hike(field, drunk, steps)
        distances.append(round(walk_simulation, 1))

    return distances


def to_graph(x, y):
    graph = figure(title='Random Walk', x_axis_label='Steps', y_axis_label='Distance')
    graph.line(x, y, legend_label='Average distance')
    show(graph)


def main(walk_distances, attempts_number, kind_of_drunk):
    average_distance_by_walk = []
    
    for steps in walk_distances:
        distances = walk_simulator(steps, attempts_number, kind_of_drunk)
        average_distances = round(sum(distances) / len(distances), 4)
        maximum_distance = max(distances)
        minimum_distance = min(distances)
        average_distance_by_walk.append(average_distances)
        print(f'{kind_of_drunk.__name__} random walk of {steps} steps')
        print(f'Average = {average_distances}')
        print(f'Max = {maximum_distance}')
        print(f'Min = {minimum_distance}')

    to_graph(walk_distances, average_distance_by_walk)

if __name__ == '__main__':
    walk_distances = [10, 100, 1000, 10000]
    attempts_number = 100

    main(walk_distances, attempts_number, TraditionalDrunk)