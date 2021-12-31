def apparently(string):
    if string.find('and') < 0 and string.find('but') < 0 or string == '':
        print('inside first if')
        return string
    string.replace('and', 'and apparently').replace('but', 'but apprently')
    return string

string = "It was great and I've never been on live television before but sometimes I don't watch this."
string2 = 'and'
string3 = 'but and apparently apparently apparently apparently'

#print('Output: ', apparently(string))

#print('Output: ',apparently(string2))

print('Output:' ,apparently(string3))
