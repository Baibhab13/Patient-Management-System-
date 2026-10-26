# WHY PYDANTIC COMES TO LIFE?

def patient_data(name, age):
    print(name)
    print(age)
    print("Data inserted to data")

'''

When a junior engineer calls the function by importing the data then by mistakenly he put the data both in string format then it will work but it is not suitable for the database with strict datatype

1st Problem : There is no type validation in python even if we mention the data type in the function it self it wont raise any typeerror.

2nd Problem : There is no data validation.
'''

