# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 00:46:41 2024

@author: HP
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, norm


# creating mock data

before= norm.rvs(loc=500,scale=100,size=100,random_state=42).astype(int)

np.random.seed(42)
after=before+ np.random.randint(low=-50,high=75,size=100)

# loc --> mean, scale --> std devation

#will create some variables in form of normal distribution


# norm.rvs() will create sample data



plt.hist(before,density=True,alpha=0.5,label="before")  # density = true give the probability density
plt.hist(after,density=True,alpha=0.5,label="after")
plt.legend()
plt.show()

before_mean=before.mean()
after_mean=after.mean()
print(before_mean,after_mean)


#set hypothesis & acceptance criteria


null_hypothesis='The mean of the before sample  is equal to the mean of the after sample '
alternate_hypothesis="the mean of the before sample  is different to the mean of the after sample"

acceptance_criteria=0.05



#hypothesis test

t_statistic, p_value =ttest_rel(before,after)
print(t_statistic,p_value)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value }is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that {null_hypothesis}")

