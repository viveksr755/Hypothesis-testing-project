# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:20:48 2024

@author: HP
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, chi2 


campaign_data=pd.read_excel("grocery_database.xlsx",sheet_name="campaign_data")


# filtering data

campaign_data= campaign_data.loc[campaign_data["mailer_type"] !="Control"]
campaign_data

# summarise to get observed ferquencies

                                     # row, col           
observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values
                                   

type(observed_values)

print(observed_values)


mailer1_signup_rate=123/(252+123)
mailer2_signup_rate=127/(209+127)
print(mailer1_signup_rate,mailer2_signup_rate)


null_hypothesis="there is no relationship between mailer type and signup rate. they are independent"

alternate_hypothesis="there is a relationship between mailer type and signup rate. they are not independent"

acceptance_criteria=0.05


# calculating expected ferquencies & chi square statistic

chi2_statistic,p_value,dof,expected_values=chi2_contingency(observed_values,correction=False)
print(chi2_statistic,p_value,dof,expected_values)

#correction = False (means "if the degress of freedom is one then always set correction to False") Yate's correction


#find the critical value for our test

critical_value= chi2.ppf(1-acceptance_criteria,dof) # ppf gives percentage point function
print(critical_value)


#print the results in the form of (Chi square stat )

if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that {alternate_hypothesis}")
else:
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that {null_hypothesis}")



# print the results in the form of  (P-value)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value }is lower than our acceptance_criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that {null_hypothesis}")




















