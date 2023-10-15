import numpy as np

lawyers = np.array([
    [3, 7, 2, 9],
    [8, 3, 6, 7],
    [4, 8, 3, 5],
    [9, 6, 5, 4]
])

weights = np.array([8, 9, 6, 7])

weightedValues = np.array([])

for lawyer in lawyers:
    weightedSum = 0

    for i, value in np.ndenumerate(lawyer):
        weight = weights[i]

        weightedSum += weight*value
    weightedValues = np.append(weightedValues, weightedSum)

print(weightedValues)

bestLawyerIndex = np.argmax(weightedValues)

print(f"\nBest lawyer is number: {bestLawyerIndex + 1}, with the value of: {weightedValues[bestLawyerIndex]}")
