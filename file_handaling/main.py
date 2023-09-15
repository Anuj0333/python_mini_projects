# # with open("../../../Documents/anuj_work\python_mini_projects/file_handaling/new_file.txt","a") as file:
# #     # contents=file.read()
# #     # print(contents)
# #     file.write("\n This is again me")

# # with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/file_handaling/weather_data.csv") as data_file :
# #     data=data_file.readlines()
# #     print(data)

# # import csv
# # with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/file_handaling/weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperatures=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas
# data=pandas.read_csv("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/file_handaling/weather_data.csv")
# # print(data ["temp"])
# # data_dict=data.to_dict()
# # print(data_dict)

# # temp_list=data["temp"].to_list()
# # print(temp_list)
# # avg_temp=sum(temp_list)/len(temp_list)
# # print(avg_temp)

# # print(data["temp"].mean())

# # print(data["temp"].max())


# #get data in ROW
# # print(data[data.day =="Monday"])
# # print(data[data["temp"]==data["temp"].max() ])

# #convert data into ferhanite
# # monday=data[data.day=="Monday"]
# # monday_temp=monday.temp[0]
# # monday_temp_F=monday_temp*9/5+32
# # print(monday_temp_F  )



# #create a dataframe from scratch
# data_dict={
#     "student":["anuj","anupriti","antima"],
#     "scores":[75,85,79]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas

data=pandas.read_csv("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/file_handaling/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squriels_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squriels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squriels_count=len(data[data["Primary Fur Color"]=="Black"])
print(gray_squriels_count)
print(black_squriels_count)
print(red_squriels_count)

data_dict={
    "fur color":["Gray","Cinnamon","Black"],
    "counts":[gray_squriels_count,red_squriels_count,black_squriels_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("C:/Users/ASUS/OneDrive/Documents/anuj_work/data/python_mini_projects.csv")