import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading data in pandas
data_2012 = pd.read_csv('data/IPD-Under-5-years-2012.csv')
data_2013 = pd.read_csv('data/IPD-Under-5-years-2013.csv')
data_2014 = pd.read_excel('data/IPD-Under-5-years-2014.xls')
data_2015 = pd.read_csv('data/IPD-Under-5-years-2015-Council.csv')

# Checking and handling any missing data
if data_2012.isnull().values.any():
    data_2012.fillna(data_2012.mean(), inplace=True)

if data_2013.isnull().values.any():
    data_2013.fillna(data_2013.mean(), inplace=True)

if data_2014.isnull().values.any():
    data_2014.fillna(data_2014.mean(), inplace=True)

if data_2015.isnull().values.any():
    data_2015.fillna(data_2015.mean(), inplace=True)

print(data_2012.tail(1))


# Analysing first ten diseases with large number of incidence
ax = plt.subplot(221)
ax1 = plt.subplot(222)
data_2012.index = data_2012['Region']
data_2013.index = data_2013['Region']
data_2012.iloc[:, 1:].sum(axis=0).sort_values(ascending=False).drop("Total", axis=0).nlargest(10).plot(kind='bar', color='red', ax=ax,  position=0, title='Top ten diseases in 2012 for IPD under 5')
data_2013.iloc[:, 1:].sum(axis=0).sort_values(ascending=False).drop("Total", axis=0).nlargest(10).plot(kind='bar', color='blue', ax=ax1, position=1, title='Top ten diseases in 2013 for IPD under 5')
ax.set_ylabel('Number of IPD')
ax1.set_ylabel('Number of IPD')
plt.tight_layout()
plt.show()

ax2 = plt.subplot(221)
ax3 = plt.subplot(222)
data_2014.index = data_2014['Region']
data_2015.index = data_2015['Council']
data_2014.iloc[:, 1:].sum(axis=0).sort_values(ascending=False).drop("Total Diagnoses", axis=0).nlargest(10).plot(kind='bar', color='green', ax=ax2,  position=2, title='Top ten diseases in 2014 for IPD under 5')
data_2015['Total'] = data_2015.sum(axis=1)
data_2015.iloc[:, 1:].sum(axis=0).sort_values(ascending=False).nlargest(10).plot(kind='bar', color='yellow', ax=ax3,  position=3, title='Top ten diseases in 2015 for IPD under 5')
ax2.set_ylabel('Number of IPD')
ax3.set_ylabel('Number of IPD')
plt.tight_layout()
plt.show()

data_2014.iloc[:, 1:].sum(axis=0).sort_values(ascending=False).drop("Total Diagnoses", axis=0).nlargest(10).plot.bar()
plt.title('Top ten diseases in 2014 for IPD under 5 IPD')
plt.ylabel('Number of IPD')
plt.show()

data_2015.iloc[:, 1:].sum(axis=0).sort_values(ascending=False).nlargest(10).plot.bar()
plt.title('Top ten diseases in 2015 for IPD under 5')
plt.ylabel('Number of IPD')
plt.show()

# Regions with large number of incidence
ax = plt.subplot(221)
ax1 = plt.subplot(222)
ax2 = plt.subplot(223)
ax3 = plt.subplot(224)
data_2012.index = data_2012['Region']
data_2013.index = data_2013['Region']
data_2014.index = data_2014['Region']
data_2015.index = data_2015['Council']
data_2012[['Region', 'Total']].sort_values(by=['Total'], ascending=False).head(5).plot(kind='bar', color='red', ax=ax,  position=1, title='Large IPD under 5yrs in 2012')
data_2013[['Region', 'Total']].sort_values(by=['Total'], ascending=False).head(5).plot(kind='bar', color='blue', ax=ax1,  position=0, title='Large IPD under 5yrs in 2013')
data_2014[['Region', 'Total Diagnoses']].sort_values(by=['Total Diagnoses'], ascending=False).head(5).plot(kind='bar', color='green', ax=ax2,  position=0, title='Large IPD under 5yrs in 2014')
data_2015['Total'] = data_2015.sum(axis=1)
data_2015[['Council', 'Total']].sort_values(by=['Total'], ascending=False).head(5).plot(kind='bar', color='yellow', ax=ax3,  position=0, title='Large IPD under 5yrs in 2015')
ax.set_ylabel('Number of IPD')
ax1.set_ylabel('Number of IPD')
ax2.set_ylabel('Number of IPD')
ax3.set_ylabel('Number of IPD')
plt.tight_layout()
plt.show()

# Regions with low number of incidence
ax = plt.subplot(221)
ax1 = plt.subplot(222)
ax2 = plt.subplot(223)
ax3 = plt.subplot(224)
data_2012.index = data_2012['Region']
data_2013.index = data_2013['Region']
data_2014.index = data_2014['Region']
data_2015.index = data_2015['Council']
data_2012[['Region', 'Total']].sort_values(by=['Total'], ascending=False).tail(5).plot(kind='bar', color='red', ax=ax,  position=1, title='Low IPD under 5yrs in 2012')
data_2013[['Region', 'Total']].sort_values(by=['Total'], ascending=False).tail(5).plot(kind='bar', color='blue', ax=ax1,  position=0, title='Low IPD under 5yrs in 2013')
data_2014[['Region', 'Total Diagnoses']].sort_values(by=['Total Diagnoses'], ascending=False).tail(5).plot(kind='bar', color='green', ax=ax2,  position=0, title='Low IPD under 5yrs in 2014')
data_2015['Total'] = data_2015.sum(axis=1)
data_2015[['Council', 'Total']].sort_values(by=['Total'], ascending=False).tail(5).plot(kind='bar', color='yellow', ax=ax3,  position=0, title='Low IPD under 5yrs in 2015')
ax.set_ylabel('Number of IPD')
ax1.set_ylabel('Number of IPD')
ax2.set_ylabel('Number of IPD')
ax3.set_ylabel('Number of IPD')
plt.tight_layout()
plt.show()
