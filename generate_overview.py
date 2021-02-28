import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

from help_functions_dashboard import convert_week_year_into_date, plot_and_save_weekly_cases

data_raw=pd.read_json('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json')
# convert string of year-week into last day of the week
data_raw['year_week']=data_raw['year_week'].apply(convert_week_year_into_date)
# set date as index
data_raw.set_index('year_week', inplace = True)

# restrict to countries of interest and columns of interest
countries_of_interest = ['DEU', 'KOR', 'GBR', 'NLD']#['DEU', 'KOR', 'ESP', 'GBR', 'NLD', 'FRA']
columns_of_interest = ['indicator','country_code',  'weekly_count', 'rate_14_day']

data_choice = data_raw.loc[data_raw.country_code.isin(countries_of_interest), columns_of_interest ]

# look at cases 
cases = data_choice.loc[data_choice.indicator == 'cases'].drop('indicator', axis=1)
# look at death
deaths = data_choice.loc[data_choice.indicator == 'deaths'].drop('indicator', axis=1)

plot_and_save_weekly_cases(cases, 'rate_14_day' )