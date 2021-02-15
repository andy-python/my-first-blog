def read_weekly_covid():
    import pandas as pd 

    covid=pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv', index_col = 'dateRep', parse_dates=True, dayfirst = True)
    covid.columns = ['year_week', 'cases_weekly', 'deaths_weekly', 'countriesAndTerritories',
       'geoId', 'countryterritoryCode', 'popData2019', 'continentExp',
       '14']

    return covid
