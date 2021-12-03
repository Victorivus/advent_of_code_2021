pb_input = open("input.txt").read().splitlines()


# Part 1

def computeEpsilonGamma(pb_input):
    gamma = []
    delta = 0.0000000000001  # it will keep 1 when 0 and 1 are equally common

    for i in range(len(pb_input[0])):
        gamma.append(round(sum(int(j[i]) for j in pb_input) / len(pb_input) + delta) % 2)
    epsilon = list(map(lambda x: (x + 1) % 2, gamma))
    return epsilon, gamma


def computeGazRating(pb_input, gazRating):
    gaz = pb_input
    for i in range(len(pb_input[0])):
        epsilon, gamma = computeEpsilonGamma(gaz)
        if gazRating == 'oxygen':
            rating = gamma
        else:
            rating = epsilon
        prev_gaz = gaz
        gaz = []
        for j in prev_gaz:
            if int(j[i]) == rating[i]:
                gaz.append(j)
        if len(gaz) == 1:
            break
    return gaz


def toDec(n):
    return int(''.join(str(e) for e in n), 2)


epsilon, gamma = computeEpsilonGamma(pb_input)

print(f'Epsilon rate is : {"".join(str(e) for e in epsilon)} ({toDec(epsilon)} in decimal)')
print(f'Gamma rate is : {"".join(str(e) for e in gamma)} ({toDec(gamma)} in decimal)')

print(f'The solution for part one is : {toDec(gamma) * toDec(epsilon)}')

# Part 2

oxygen = computeGazRating(pb_input, 'oxygen')
co2 = computeGazRating(pb_input, 'co2')

print(f'Oxygen rate is : {"".join(str(e) for e in oxygen)} ({toDec(oxygen)} in decimal)')
print(f'CO2 rate is : {"".join(str(e) for e in co2)} ({toDec(co2)} in decimal)')

print(f'The solution for part two is : {toDec(oxygen) * toDec(co2)}')
