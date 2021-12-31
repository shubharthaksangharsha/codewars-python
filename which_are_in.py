def in_array(array1, array2):
    #method1 using for loop 
#    result = []
#    lst = []
#    for x in array1:
#        for y in array2:
#            if x in y:
#                lst.append(x)
#    [result.append(x) for x in lst if x not in result]    
#    return sorted(result)
    
    #method 2 using list comprehension
    #result = []
    #lst = [x for y in array2  for x in array1 if x in y]
    #[result.append(x) for x in lst if x  not in result]
    #result.sort()
    #return sorted(result)

    #method3 one-line solution
    return sorted({x for x in array1 if any(x in y for y in array2)})
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))

