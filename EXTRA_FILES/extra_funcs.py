import random


def rand(**args):
    a_sum = sum(args.values())
    if a_sum != 100:
        raise Exception("Wrong 'values' probabilities.\nValues: {0}\nSum: {1}".format(args.values(), a_sum))

    prob = 100
    for key, value in args.items():
        a = random.randint(0, prob)
        if a <= value:
            return key
        else:
            prob -= value


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)
