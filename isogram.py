def is_isogram(string):
    if string == '':
          return True
    new_string = string.upper()
    print(new_string)
    for i in new_string:
          if new_string.count(i) >= 2:
               return False
    return True
string = input("Please enter a string: ")
print(is_isogram(string))
