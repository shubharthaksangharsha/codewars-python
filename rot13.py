def rot(message, key=13):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    mylowerdict = {alphabet[i]:alphabet[(i+key)% 26] for i,c in enumerate(alphabet)}
    myupperdict = {i.upper():v.upper() for i,v in mylowerdict.items()}
    mylowerdict.update(myupperdict)
    return "".join([ mylowerdict.get(x,x) for x in message])    
message = input()
print(rot(message,1))
