""" Task: I need a python function named get_bucket_name that can receive a string value as argument.
    The string value has a pattern. The pattern is that the value will have several words that are separated by a delimiter "-".
    E.x. I-am-trying-to-do-a-task.
    First task is that the function should print all the words in the string as a list."""

def get_bucket_name(string):
    list=string.split("-")
    #print(list)
    print(list[:4])
str=input("Enter the string: ")
get_bucket_name(str)




