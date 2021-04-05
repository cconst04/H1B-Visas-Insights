import pandas as pd
import math
from matplotlib import pyplot as plt
import re

def clear_html(raw_html):
	#cleaning is done only for strings
	if type(raw_html) != str:
		return raw_html
	cleanr = re.compile('(<.*?>)+')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def clear_soc_code(x):
	x = clear_html(x)
	if x == 'OPERATIONS RESEARCH ANALYSTS':
		return 15
	elif type(x) == str and '-' in x:
		return int(x.split('-')[0])
	return x

def to_yearly_wage(row):
	wage_from = cols[year]['wage_from']
	wage_unit = cols[year]['wage_unit']
	for c in ['$', ',']:
		row[wage_from] = str(row[wage_from]).replace(c, '')
		if year <= 2016:
			row[wage_from] = row[wage_from].split('-')[0].strip()
	if row[wage_from] == '':
		return None
	elif math.isnan(float(row[wage_from])):
		return float(row[wage_from])
	elif row[wage_unit] == 'Hour':
		return int(float(row[wage_from])) * 24 * 365
	elif row[wage_unit] == 'Month':
		return int(float(row[wage_from])) * 12
	elif row[wage_unit] == 'Weekly':
		return int(float(row[wage_from]) / 7 * 365)
	elif row[wage_unit] == 'Bi-Weekly':
		return int(float(row[wage_from]) / 14 * 365)
	return int(float(row[wage_from]))

def codes_to_names(code):
	return job_codes[code] if code in job_codes else code 

cols = {
	2020:{
		'wage_from': 'WAGE_RATE_OF_PAY_FROM',
		'wage_unit': 'WAGE_UNIT_OF_PAY',
		'soc_code': 'SOC_CODE',
		'case_status': 'CASE_STATUS'
	},
	2019:{
		'wage_from': 'WAGE_RATE_OF_PAY_FROM_1',
		'soc_code': 'SOC_CODE',
		'wage_unit': 'WAGE_UNIT_OF_PAY_1',
		'case_status': 'CASE_STATUS'

	},
	2018:{
		'wage_from': 'WAGE_RATE_OF_PAY_FROM',
		'wage_unit': 'WAGE_UNIT_OF_PAY',
		'soc_code': 'SOC_CODE',
		'case_status': 'CASE_STATUS'
	},
	2017:{
		'wage_from': 'WAGE_RATE_OF_PAY_FROM',
		'wage_unit': 'WAGE_UNIT_OF_PAY',
		'soc_code': 'SOC_CODE',
		'case_status': 'CASE_STATUS'

	},
	2016:{
		'wage_from': 'WAGE_RATE_OF_PAY_FROM',
		'wage_unit': 'WAGE_UNIT_OF_PAY',
		'soc_code': 'SOC_CODE',
		'case_status': 'CASE_STATUS'

	},
	2015:{
		'wage_from': 'WAGE_RATE_OF_PAY',
		'wage_unit': 'WAGE_UNIT_OF_PAY',
		'soc_code': 'SOC_CODE',
		'case_status': 'CASE_STATUS'

	},
	2014:{
		'wage_from': 'LCA_CASE_WAGE_RATE_FROM',
		'wage_unit': 'LCA_CASE_WAGE_RATE_UNIT',
		'soc_code': 'LCA_CASE_SOC_CODE',
		'case_status': 'STATUS'

	},
	2013:{
		'wage_from': 'LCA_CASE_WAGE_RATE_FROM',
		'wage_unit': 'LCA_CASE_WAGE_RATE_UNIT',
		'soc_code': 'LCA_CASE_SOC_CODE',
		'case_status': 'STATUS'

	}
}

useful_cols = {
	2020: [
		'SOC_CODE',
		'CASE_NUMBER',
		'CASE_STATUS',
		'FULL_TIME_POSITION',
		'BEGIN_DATE',
		'END_DATE',
		'EMPLOYER_NAME',
		'EMPLOYER_STATE',
		'WAGE_RATE_OF_PAY_FROM',
		# 'WAGE_RATE_OF_PAY_TO_1',
		'WAGE_UNIT_OF_PAY',
		'NAICS_CODE',
		'FULL_TIME_POSITION'
	],
	2019:[
		'SOC_CODE',
		'CASE_NUMBER',
		'CASE_STATUS',
		'FULL_TIME_POSITION',
		'PERIOD_OF_EMPLOYMENT_START_DATE',
		'PERIOD_OF_EMPLOYMENT_END_DATE',
		'EMPLOYER_NAME',
		'EMPLOYER_STATE',
		'WAGE_RATE_OF_PAY_FROM_1',
		'WAGE_UNIT_OF_PAY_1',
		'NAICS_CODE',
		'FULL_TIME_POSITION'
	],
	2018:[
		'SOC_CODE',
		'CASE_NUMBER',
		'CASE_STATUS',
		'FULL_TIME_POSITION',
		'EMPLOYMENT_START_DATE',
		'EMPLOYMENT_END_DATE',
		'EMPLOYER_NAME',
		'EMPLOYER_STATE',
		'WAGE_RATE_OF_PAY_FROM',
		'WAGE_UNIT_OF_PAY',
		'NAICS_CODE',
		'FULL_TIME_POSITION'
	],
	2017:[
		'SOC_CODE',
		'CASE_NUMBER',
		'CASE_STATUS',
		'FULL_TIME_POSITION',
		'EMPLOYMENT_START_DATE',
		'EMPLOYMENT_END_DATE',
		'EMPLOYER_NAME',
		'EMPLOYER_STATE',
		'WAGE_RATE_OF_PAY_FROM',
		'WAGE_UNIT_OF_PAY',
		'NAICS_CODE',
		'FULL_TIME_POSITION'
	],
	2016:[
		'SOC_CODE',
		'CASE_NUMBER',
		'CASE_STATUS',
		'FULL_TIME_POSITION',
		'EMPLOYMENT_START_DATE',
		'EMPLOYMENT_END_DATE',
		'EMPLOYER_NAME',
		'EMPLOYER_STATE',
		'WAGE_RATE_OF_PAY_FROM',
		'WAGE_UNIT_OF_PAY',
		'NAIC_CODE',
		'FULL_TIME_POSITION'
	],
	2015:[
		'SOC_CODE',
		'CASE_NUMBER',
		'CASE_STATUS',
		'FULL_TIME_POSITION',
		'EMPLOYMENT_START_DATE',
		'EMPLOYMENT_END_DATE',
		'EMPLOYER_NAME',
		'EMPLOYER_STATE',
		'WAGE_RATE_OF_PAY',
		'WAGE_UNIT_OF_PAY',
		'NAIC_CODE',
		'FULL_TIME_POSITION'
	],
	2014:[
		'LCA_CASE_SOC_CODE',
		'LCA_CASE_NUMBER',
		'STATUS',
		'FULL_TIME_POS',
		'LCA_CASE_EMPLOYMENT_START_DATE',
		'LCA_CASE_EMPLOYMENT_END_DATE',
		'LCA_CASE_EMPLOYER_NAME',
		'LCA_CASE_EMPLOYER_STATE',
		'LCA_CASE_WAGE_RATE_FROM',
		'LCA_CASE_WAGE_RATE_UNIT',
		'LCA_CASE_NAICS_CODE',
		'FULL_TIME_POS'
	],
	2013:[
		'LCA_CASE_SOC_CODE',
		'LCA_CASE_NUMBER',
		'STATUS',
		'FULL_TIME_POS',
		'LCA_CASE_EMPLOYMENT_START_DATE',
		'LCA_CASE_EMPLOYMENT_END_DATE',
		'LCA_CASE_EMPLOYER_NAME',
		'LCA_CASE_EMPLOYER_STATE',
		'LCA_CASE_WAGE_RATE_FROM',
		'LCA_CASE_WAGE_RATE_UNIT',
		'LCA_CASE_NAICS_CODE',
		'FULL_TIME_POS'
	],
}


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
for year in range(2020, 2021):
	print(year)
	data = pd.read_csv('csv/{}.csv'.format(year))
	print("{}:Dataset rows:{}".format(year, len(data)))
	data.dropna(how='all', inplace=True)
	data = data[useful_cols[year]]
	# for col in data:
	# 	data[col].apply(lambda row: clear_html(row))
	#drop withdrawn cases
	status_col = cols[year]['case_status']
	data = data[~data[status_col].str.contains('WITHDRAWN')]
	#get the digits before the dash of the soc_code
	data[cols[year]['soc_code']] = data[cols[year]['soc_code']].apply(clear_soc_code)
	#clean the wage and conver it to year rate
	data[cols[year]['wage_from']] = data.apply(lambda row: to_yearly_wage(row), axis=1)
	data[cols[year]['wage_unit']] = 'Year'

	#replace the soc code with the general name of the job
	# data[cols[year]['soc_code']].apply(lambda x: codes_to_names(x))

	print("New dataset size:{}".format(len(data)))
	data.columns = useful_cols[2020]
	sample = data.sample(n=100)
	data.to_csv('csv/processed_{}.csv'.format(year))
	# for col in data.columns:
	# 	print(col)