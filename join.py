"""
delimiter=input("Enter the delimiter: ")
str=delimiter.join(list)
print(str)
"""
def join (string):
    list=str.split("-")
    list=list[:4]
    result=".".join(list)
    return result

str="arun-is-a-good-bad-boy"
print(join(str))
