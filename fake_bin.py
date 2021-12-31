def fake_bin(x):
    answer= [1 if int(a)>=5 else 0 for a in x]
    return "".join(str(x) for x in answer)

