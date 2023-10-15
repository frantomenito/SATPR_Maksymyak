import numpy as np

lawyers = np.array([
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]
])

maxingPattern = np.array([True, False, True, True, True])
weights = np.array([7, 5, 6, 8, 6])

# Finding min and max for every column
minimums = np.min(lawyers, axis=0)
maximums = np.max(lawyers, axis=0)

# Normalizing values
normalizedValues = np.zeros((lawyers.shape[0], lawyers.shape[1]))

for i, isMaxingCurrentColumn in np.ndenumerate(maxingPattern):
    value = 0

    if isMaxingCurrentColumn:
        value = (lawyers[:, i] - minimums[i]) / (maximums[i] - minimums[i])
    else:
        value = (maximums[i] - lawyers[:, i]) / (maximums[i] - minimums[i])

    normalizedValues[:, i] = value

print(normalizedValues)

weightedValues = np.sum(normalizedValues * weights, axis=1)

bestLawyerIndex = np.argmax(weightedValues)

print(f"\nBest lawyer is number: {bestLawyerIndex + 1}, with the value of: {weightedValues[bestLawyerIndex]}")