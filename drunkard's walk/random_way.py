from drunk import TraditionalDrunk
from field import Field
from coordinates import Coordinates
from bokeh.plotting import figure, show
from bokeh.models import Range1d


def hike(field, drunk, steps):
    x_steps = []
    y_steps = []
    start = field.get_coordinate(drunk)

    for _ in range(steps):
        field.move_drunk(drunk)
        x_steps.append(field.get_coordinate(drunk).x)
        y_steps.append(field.get_coordinate(drunk).y)
    
    return (start.distance(field.get_coordinate(drunk)), x_steps, y_steps)


def walk_simulator(steps, attempts_number, kind_of_drunk):
    
    drunk = kind_of_drunk(name='Jim')
    origin = Coordinates(0, 0)
    distances = []
    roads = []
    
    for _ in range(attempts_number):
        field = Field()
        field.add_drunk(drunk, origin)
        walk_simulation, x_steps, y_steps = hike(field, drunk, steps)
        distances.append(round(walk_simulation, 1))
        roads.append([x_steps, y_steps])

    return (distances, roads)


def to_graph(walk_distances, average_distance_by_walk, roads, attempts_number):
    graph = figure(title='Random Walk', x_axis_label='Steps', y_axis_label='Distance', name='Average Distances')
    graph.line(walk_distances, average_distance_by_walk, legend_label='Average distance')
    graphs = []
    graphs.append(graph)
    
    for attempt in range(attempts_number):
        path = figure(title=f'Drunk Road, Attempt {attempt + 1}',
                    x_axis_label='Steps on x',
                    y_axis_label='Steps on y',
                    name='Path of drunk',
                    x_range= Range1d(start=-50, end=50),
                    y_range=Range1d(start=-50, end=50))
        path.line([0, 0], [-100, 100], line_color='black', line_width=1, line_dash='solid')
        path.line([-100, 100], [0, 0], line_color='black', line_width=1, line_dash='solid')

        for steps in walk_distances:
            if steps == 10: 
                path.line(roads[0][attempt][0], roads[0][attempt][1], legend_label='Steps: 10', line_color='green')
            elif steps == 100:
                path.line(roads[1][attempt][0], roads[1][attempt][1], legend_label='Steps: 100', line_color='yellow')
            else:
                path.line(roads[2][attempt][0], roads[2][attempt][1], legend_label='Steps: 1000', line_color='red')
        
        graphs.append(path)
    
    show(graphs)


def main(walk_distances, attempts_number, kind_of_drunk):
    average_distance_by_walk = []
    roads = []
    
    for steps in walk_distances:
        distances, roads_received = walk_simulator(steps, attempts_number, kind_of_drunk)
        average_distances = round(sum(distances) / len(distances), 4)
        maximum_distance = max(distances)
        minimum_distance = min(distances)
        average_distance_by_walk.append(average_distances)
        roads.append(roads_received)
        print(f'{kind_of_drunk.__name__} random walk of {steps} steps')
        print(f'Average = {average_distances}')
        print(f'Max = {maximum_distance}')
        print(f'Min = {minimum_distance}')

    to_graph(walk_distances, average_distance_by_walk, roads, attempts_number)


if __name__ == '__main__':
    walk_distances = [10, 100, 1000]
    attempts_number = 10

    main(walk_distances, attempts_number, TraditionalDrunk)
