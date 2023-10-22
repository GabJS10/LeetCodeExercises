import pandas as pd

def selectData(students):

    #setear cual el indice por el cual queremos buscar
    students.set_index("student_id",inplace=True)

    #con loc, seleccionamos las filas que cumplan la condicion y las columnas que queremos ver
    result = students.loc[[101],["name","age"]]

    #return students[students['student_id'] == 101][['name', 'age']]
    return result