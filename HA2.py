
import pandas as pd
import numpy as np
#1 To create series object in pandas we can use these types of data: tuple, dictionary, List, NumPy array

#2
months_names = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
months_numbers = list(range(1,13))
months_series = pd.Series(data=months_numbers, index=months_names)
print(months_series)

#3
students = {
    "MatMIE": 34,
    "MatDAIS": 35,
    "COMIE" : 41,
    "COMEC": 46
}
students_series = pd.Series(students)
print(students_series)

#4
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_dataframe = pd.DataFrame(exam_data, index=labels)
print(exam_dataframe)

#5
manyAttempts = exam_dataframe[exam_dataframe['attempts'] > 2]
print("Number of attempts in the examination is greater than 2:")
print(manyAttempts)