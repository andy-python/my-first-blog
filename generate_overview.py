# Create script that creates covid overview data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry_convert as pc

import weekly_covid
covid = weekly_covid.read_weekly_covid()


#===============================
# Look at Germany
germany = covid.loc[covid.geoId == 'DE']
nl = covid.loc[covid.geoId == 'NL']
es = covid.loc[covid.geoId == 'ES']
uk = covid.loc[covid.geoId == 'UK']
kr = covid.loc[covid.geoId == 'KR']
#===============================

fig, _ = plt.subplots(1,2,figsize=(15,5), sharey = True)

plt.subplot(1,2,1)
# plt.margins(0.02)


_=germany['14'].plot()
_=es['14'].plot()
_=nl['14'].plot()
_=uk['14'].plot()
_=kr['14'].plot()
plt.legend(['de', 'es', 'nl', 'uk', 'kr'])

plt.ylabel('Daily cases per 100K / flattened')
plt.xlabel(' ')

plt.title('Whole pandemie')
# ========================
plt.subplot(1,2,2)

germany['14'].plot()
_=es['14'].plot()
_=nl['14'].plot()
_=uk['14'].plot()
_=kr['14'].plot()
plt.legend(['Germany', 'Spain', 'Netherlands', 'UK', 'South Korea'])

plt.xlim(['Oct 2020', max(uk.index)])
plt.xlabel(' ')

plt.title('Zoom in: Since October')


plt.show()

fig.savefig( 'test.jpg', bbox_inches='tight');