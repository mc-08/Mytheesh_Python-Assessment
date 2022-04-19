from scipy import stats
Probability = stats.poisson.cdf(80,76)
print("The probability that the number of pizza sales exceeds 80 in a day",Probability)
