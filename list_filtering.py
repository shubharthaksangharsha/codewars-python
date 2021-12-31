def filter_list(l):
    #solution 1:-
    new_list = []
    for i in l:
        if isinstance(i, int):
            new_list.append(i)
    return new_list
   #solution2:-
   #new_list = []
   #for i in l:
    #   if type(i) is not str:
     #      new_list.append(i)
   #return new_list
