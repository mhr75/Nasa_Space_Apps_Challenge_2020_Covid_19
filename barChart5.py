import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("turnOver.csv")

df = data['GEO']
#print (df)
data = data.dropna(axis=0,how='any')
#print(data)
for index, row in data.iterrows():
    #print(row['CURRENCY'])
    objects = ('2019Q1', '2020Q1')
    y_pos = np.arange(len(objects))
    performance = (row['2019Q1'],row['2020Q1'])
    #print(performance)
    plt.bar(y_pos, performance, align='center', color=[ 'black','maroon'])
    plt.xticks(y_pos, objects)
    plt.ylabel(row['GEO'])
    plt.title('Turn Over Rate')
    plt.savefig('NASAAA %s_turn.png' % row['GEO'])
    plt.show()

# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
#
# plt.show()