from random import random, randint, seed, uniform


def warp(min, max, random_seed, warped_list, by_integers=False):
    seed(random_seed)
    final_list = []
    if by_integers is True:
        perturbation_list = [randint(min, max) for _ in warped_list]
    else:
        perturbation_list = [uniform(min, max) for _ in warped_list]
    for x, y in zip(warped_list, perturbation_list):
        final_list.append(x + y)
    return final_list


# ###DEMO###
# warp(-0.9, 0.9, 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# warp(-4, 4, 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], by_integers=True)
