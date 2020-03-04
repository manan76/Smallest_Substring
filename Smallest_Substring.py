
def SmallestSub(str):
    result = [str[i: j] for i in range(len(str))
           for j in range(i + 1, len(str) + 1)]
    max=0
    for i in range(len(result)):
        se=len(set(result[i]))
        le=len(result[i])
        if(se==le):
            if(max<se):
                max=se
    return max


st=input()
print(SmallestSub(st))