# functions for the corona dashboard

# pure function that converts week number into last day of week as datetime object
def convert_week_year_into_date(year_week):
    import datetime
    delta= datetime.timedelta(1)
    return datetime.datetime.strptime(year_week + '-1', "%Y-%W-%w") -delta

# function that plots dashboard and creates output file
def plot_and_save_weekly_cases(cases, column):

    import matplotlib.pyplot as plt 
    
    fig, _ = plt.subplots(1,1,figsize=(15,5), sharey = True)

    import seaborn as sns
    sns.lineplot(data = cases, y = 'rate_14_day', x = cases.index, hue = 'country_code')
    plt.title('Daily cases / 100K (flattened, per week)')
    plt.xlabel('')
    plt.show()

    fig.savefig( 'dashboard.jpg', bbox_inches='tight');
    return