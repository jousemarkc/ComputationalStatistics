import random


def throw_dice(throws_number):
    throws_secuence = []

    for _ in range(throws_number):
        throw = random.choice([1, 2, 3, 4, 5, 6])
        throws_secuence.append(throw)

    return throws_secuence


def main(attempts_number, throws_number):
    throws = []

    for _ in range(attempts_number):
        throws_secuence = throw_dice(throws_number)
        throws.append(throws_secuence)

    throws_with_1 = 0

    for throw in throws:
        if 1 in throw:
            throws_with_1 += 1

    probabilities_throws_with_1 = throws_with_1 / attempts_number
    print(f'The probability of get leastwise a 1 in {throws_number} throws = {probabilities_throws_with_1}')



if __name__ == '__main__':
    throws_number = int(input('How many throws of the dice?: '))
    attempts_number = int(input('How many times will the simulation run?: '))

    main(attempts_number, throws_number)