# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 00:27:14 2024

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm


# creating mock data

sample_A= norm.rvs(loc=500,scale=100,size=250,random_state=42).astype(int)

sample_B= norm.rvs(loc=550,scale=150,size=100,random_state=42).astype(int)

# loc --> mean, scale --> std devation

#will create some variables in form of normal distribution


# norm.rvs() will create sample data



plt.hist(sample_A,density=True,alpha=0.5)  # density = true give the probability density
plt.hist(sample_B,density=True,alpha=0.5)
plt.show()

sample_A_mean=sample_A.mean()
sample_B_mean=sample_B.mean()
print(sample_A_mean,sample_B_mean)


#set hypothesis & acceptance criteria


null_hypothesis='The mean of the sample A is equal to the mean of the sample_B'
alternate_hypothesis="the mean of the sample A is different to the mean of the sample_B"

acceptance_criteria=0.05



#hypothesis test

t_statistic, p_value =ttest_ind(sample_A,sample_B)
print(t_statistic,p_value)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value }is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that {null_hypothesis}")




# Welch's t-test (commenly used independent t-test)


#hypothesis test

t_statistic, p_value =ttest_ind(sample_A,sample_B,equal_var=False)
print(t_statistic,p_value)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value }is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that {null_hypothesis}")






















