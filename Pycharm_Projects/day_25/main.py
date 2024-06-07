# # import csv
# # with open ("weather_data.csv",) as data_fies :
# #     data = csv.reader(data_fies)
# #     for row in data:
# #         print(row)
# #
# import numpy as np
# # import pandas as pd
# # df=pd.read_csv('weather_data.csv')
# # print(df)
# # temp=df['temp'].to_list()
# # print(temp)
# # avg_temp=np.sum(temp)/len(temp)
# # print(avg_temp)
# #
# #
# # counter=0
# # for ele in temp:
# #     counter+=ele
# # print(f"Average temperature = {round(counter/len(temp),6)}")
# # print(df.columns)
# #
# #
# # print(np.mean(temp))
# # print(sum(temp))
# #
# # ser=df['temp']
# # print(f"the maximum value in series is {ser.max()}")
# import pandas as pd
# df=pd.read_csv('weather_data.csv')
# a=df.query("day=='Monday'")
# #print(type(a))
# centigrade=a.temp.values
# faren = centigrade* 1.8000 + 32.00
# print(faren[0])


import pandas as pd
data_frame= pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#print(data_frame['Primary Fur Color']=='Gray')
# data=data_frame[data_frame['Primary Fur Color']=='Gray']['Primary Fur Color']
# print(data)
# group =data_frame.groupby(data_frame['Primary Fur Color'])
# print(group.count())

grey_squirrel=len(data_frame[data_frame['Primary Fur Color']=='Gray'])
cinnamon_squirrel=len(data_frame[data_frame['Primary Fur Color']=='Cinnamon'])
black_squirrel =len(data_frame[data_frame['Primary Fur Color']=='Black'])
print(grey_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

dict_data ={"Color":["Gray","Cinnamon","Black"],
            "Count":[grey_squirrel,cinnamon_squirrel,black_squirrel]
}

new_data_frame =pd.DataFrame(dict_data)
#new_data_frame.to_csv('new_data.csv')
print(new_data_frame)
