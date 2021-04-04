import pandas as pd
import math
from matplotlib import pyplot as plt
def clear_soc_code(x):
	if x == 'OPERATIONS RESEARCH ANALYSTS':
		return 15
	elif type(x) == str and '-' in x:
		return int(x.split('-')[0])
	return x

def to_yearly_wage(row):
	for c in ['$', ',']:
		row.WAGE_RATE_OF_PAY_FROM_1 = str(row.WAGE_RATE_OF_PAY_FROM_1).replace(c, '')
	if row.WAGE_UNIT_OF_PAY_1 == 'Hour':
		return int(float(row.WAGE_RATE_OF_PAY_FROM_1)) * 24 * 365
	elif row.WAGE_UNIT_OF_PAY_1 == 'Month':
		return int(float(row.WAGE_RATE_OF_PAY_FROM_1)) * 12
	if math.isnan(float(row.WAGE_RATE_OF_PAY_FROM_1)):
		return float(row.WAGE_RATE_OF_PAY_FROM_1)
	return int(float(row.WAGE_RATE_OF_PAY_FROM_1))

cols = [
	'SOC_CODE',
	'CASE_NUMBER',
	'CASE_STATUS',
	'FULL_TIME_POSITION',
	'PERIOD_OF_EMPLOYMENT_START_DATE',
	'PERIOD_OF_EMPLOYMENT_END_DATE',
	'EMPLOYER_NAME',
	'EMPLOYER_STATE',
	'WAGE_RATE_OF_PAY_FROM_1',
	'WAGE_RATE_OF_PAY_TO_1',
	'WAGE_UNIT_OF_PAY_1',
	'NAICS_CODE'
]

job_codes = {
	11: 'Management',
	13: 'Financial Operations',
	23: 'Legal Occupations',
	15: 'Computer and Maths',
	16: 'Architecture and Engineering',
	17: 'Life',
	18: 'Physical',
	19: 'Social Science',
	21: 'Community and Social service',
	29: 'Healthcare Practitioners and Technical',
	31: 'Support Occupations',
	25: 'Education', #?
	26: 'Training', #?
	27: 'Library', #?
	51: 'Production Occupations',
	55: 'Military Specific Occupations'
}
data = pd.read_csv('data/H-1B_Disclosure_Data_FY2019.csv')
print("Dataset rows:{}".format(len(data)))
data.dropna(how='all', inplace=True)
data['SOC_CODE'] = data['SOC_CODE'].apply(clear_soc_code)
data['WAGE_RATE_OF_PAY_FROM_1'] = data.apply(lambda row: to_yearly_wage(row), axis=1)
data['WAGE_UNIT_OF_PAY_1'] = 'Year'
print("New dataset size:{}".format(len(data)))
sample = data.sample(n=100)
for col in data.columns:
	print(col)
# hist = data['WAGE_RATE_OF_PAY_FROM_1'].hist()
plt.boxplot(data['WAGE_RATE_OF_PAY_FROM_1'].dropna())
plt.show()
breakpoint()