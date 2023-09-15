# num=[1,2,3]
# new_list=[n+1 for n in num]
# print(new_list)



# st="anuj kumar gupta"
# new_st=[letter for letter in st]
# print(new_st)

# range=[n*2 for n in range(1,5 )]
# print(range)


# #conditional list comprehension
# names=["anuj","anupriti","antima","srijan","sajal","dev"]
# short_names=[name.upper() for name in names if (len(name)>=6)]
# print(short_names)

# #dictionary comprehension
# import random
# names=["anuj","anupriti","antima","srijan","sajal","dev"]
# student_score={students:random.randint(1,100) for students in names}
# passed_students={student:scores for (student,scores) in student_score.items() if scores>=60}
# print(student_score)
# print(passed_students)



student_dict={"student":["anuj","anupriti","antima","srijan","sajal","dev"],
              "score":[75,85,79,83,82,88]
              }
#  looping through dictionaries:
# for (keys,values) in student_dict.items():
#     print(keys,values)


import pandas
student_data_frame=pandas.DataFrame(student_dict)
# print(student_data_frame)

# looping through data frame
# for (key,value) in student_data_frame.items():
#     print(key,value)

#loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student=="anuj":
        print(row.score)