import random


def rand(**args):
    sum(args.values())
    if sum != 100:
        raise Exception("Wrong values' probabilities")

    prob = 100
    for key, value in args.items():
        a = random.randint(0, prob)
        if a <= value:
            return key
        else:
            prob -= value
