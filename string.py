str1 = "nagendra"
str2 = 'my name is nagendra'
str3 = "nagendra's"
multilineStr = '''This is example is
demo how to use 
multi line in python'''

 
print(str1[0]) # prints the 1st character 'n'
print(str1[-1]) # prints the last character 'a'
print(str1[0:5])  # start from index 0 to length 5, prints 'nagen'
print(str1[:5])   # same as above
print(str1[0:])  # start from index 0 to end, prints 'nagendra'
print(str1[0:-1])  # start from index 0 to , prints 'nagendr'
print(str1[:]) # is valid and prints the full string
