import pandas as pd

def createDataframe(student_data):
     return pd.DataFrame(student_data,columns=["student_id","age"])
     


print(createDataframe([[1,15],[2,11],[3,11],[4,20]]))