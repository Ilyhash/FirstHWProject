import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--task', type=str, dest='task', default='vowels')
PARSER.add_argument('--arg', type=str, dest='arg')

ARG = PARSER.parse_args()


def vowels(given_string):
    count = 0
    for i in given_string.lower():
        if i in ['a', 'o', 'u', 'i', 'y', 'e']:
            count += 1
    print(count)


def perfect_power(number):
    pass


def lazy(number):
    print(sum(range(number + 1))+1)


if ARG.task == 'vowels':
    vowels(ARG.arg)
elif ARG.task == 'perfect':
    perfect_power(ARG.arg)
elif ARG.task == 'lazy':
    lazy(ARG.arg)
