import random, math
from statistic import standard_deviation, mean


def throw_down_needles(needles_number):
    inside_circle = 0

    for _ in range(needles_number):
        x = random.random() * random.choice([1, -1])
        y = random.random() * random.choice([1, -1])
        distance_from_center = math.sqrt(x**2 + y**2)

        if distance_from_center <= 1:
            inside_circle += 1  

    return 4 * (inside_circle) / needles_number


def estimation(needles_number, attempts_number):
    estimated = []

    for _ in range(attempts_number):
        estimate_pi = throw_down_needles(needles_number)
        estimated.append(estimate_pi)

    estimated_mean = mean(estimated)
    estimated_sigma = standard_deviation(estimated)
    print(f'Estimate: {round(estimated_mean, 5)}, Standard Deviation: {round(estimated_sigma, 5)}, Thrown needles: {needles_number}')
    
    return (estimated_mean, estimated_sigma)


def estimate_pi(precision, attempts_number, needles_number):
    sigma = precision

    while sigma >= precision / 1.96:
        mean, sigma = estimation(needles_number, attempts_number)
        needles_number *= 2

    return mean


if __name__ == '__main__':
    estimate_pi(0.01, 11, 1000)