## 1. Introduction ##

import pandas as pd 
housing = pd.read_csv('housing.csv')

housing.head()
housing.tail()

housing.info()

## 2. Seaborn ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
housing = pd.read_csv('housing.csv')

sns.set_theme()
sns.relplot(data = housing, x = 'Gr Liv Area', y = 'SalePrice')
plt.show()

correlation = 'positive'

## 3. Variable Representation: Color ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
sns.set_theme()
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice', hue = 'Overall Qual', palette = 'RdYlGn')
plt.show()

sentence_1 = True
sentence_2 = True