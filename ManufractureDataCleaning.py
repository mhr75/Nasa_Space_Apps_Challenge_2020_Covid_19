
import pandas as pd
import numpy as np
data = pd. read_csv("Manufractrure.csv")

data = data.sort_values(by=["GEO","TIME"])
df = data[data.Value != ":"]
#df['Value'] = df['Value'].str.replace(" ","")
country = df["GEO"].unique();
#print(country)
main_result = pd.DataFrame()
for x in country:
   df2 = df[df["GEO"]==x]
   df3 = df2[df2.TIME.str.contains('2019')]
   avg = np.array(df3['Value'].astype(float))
   avg = avg.mean()
   #print(avg)
   df4 = df2[df2.TIME.str.contains('2020')]
   avg2 = np.array(df4['Value'].astype(float))
   avg2 = avg2.mean()
   #print(avg2)
   #d = {'col1': [1, 2], 'col2': [3, 4]}
   #df = pd.DataFrame(data=d)
   resultRow = {'GEO':[x],'2019(mean)':[avg],'2020(mean)':[avg2]}
   result = pd.DataFrame(data=resultRow)
   main_result = pd.concat([main_result,result])


main_result.to_csv("importPriceMean.csv",index=False)

