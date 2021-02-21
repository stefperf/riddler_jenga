# https://fivethirtyeight.com/features/can-you-win-riddler-jenga/


import random


HALF_LENGTH = 1.  # length of half a block; it does not influence the result


def jenga_up(debug=False, stop=None):
    centers = [0]
    barycenters = [0]
    n = 1
    while True:
        new_center = centers[-1] + random.uniform(-HALF_LENGTH, +HALF_LENGTH)
        centers.append(new_center)
        for k in range(1, n + 1):
            barycenters[-k] = (k * barycenters[-k] + new_center) / (k + 1)
        barycenters.append(new_center)
        n += 1
        stands = all([c - HALF_LENGTH <= b <= c + HALF_LENGTH for c, b in zip(centers[:-1], barycenters[1:])])
        if not stands or n == stop:
            if debug:
                print()
                print([abs(b - c) <= 1. for c, b in zip(centers[:-1], barycenters[1:])])
                print(stands)
            return n


def run_stats(freqs=False):
    runs = 0
    counts = {}
    while True:
        runs += 1
        n = jenga_up()
        counts[n] = counts.get(n, 0) + 1
        if not runs % 1000000:
            print(f'\nResult after {runs // 1000000} million runs:')
            average = 0.
            for n in sorted(counts.keys()):
                freq = counts[n] / runs
                average += n * freq
                if freqs:
                    print(f'{n} => {freq}')
            print(f'average blocks at fall = {average}')


run_stats()
