def alphabet_position(text):        
    def to_num(c):
        c = c.lower()
        return ord(c) - ord('a') + 1
    mylist = (to_num(c) for c in text if c.isalpha()) 
    return ' '.join([str(x) for x in mylist])
text = ""
print(alphabet_position(text))
