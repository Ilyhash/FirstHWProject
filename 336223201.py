import argparse

PARSER = argparse.ArgumentParser('function assignment')
PARSER.add_argument('--task', type=str, dest='task')
PARSER.add_argument('--arg', type=str, dest='arg')

ARG = PARSER.parse_args()


def vowels(given_string: str):
    count = 0
    for i in given_string.lower():
        if i in ['a', 'o', 'u', 'i', 'y', 'e']:
            count += 1
    print(count)


def perfect_power(num: int):
    perf_powers = [1]
    candidate = 4
    number = int(num)
    while len(perf_powers) < number:
        done = False
        for i in range(2, candidate // 2 + 1):
            if candidate % i == 0:
                check = candidate / i
                while check % i == 0 and check > 1:
                    check = check / i
                    if check == 1:
                        perf_powers.append(candidate)
                        done = True
            if done:
                break
        candidate += 1
    print(perf_powers[-1])


def lazy(number: int):
    print(sum(range(number + 1))+1)


if ARG.task == 'vowels':
    vowels(ARG.arg)
elif ARG.task == 'perfect':
    perfect_power(ARG.arg)
elif ARG.task == 'lazy':
    lazy(ARG.arg)
