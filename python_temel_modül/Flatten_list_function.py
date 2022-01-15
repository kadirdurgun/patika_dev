
array = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]



def isList(array):
    if type(array) == list:
        return True
    else:
        return False

def FlattenList(array):
    for i in range(0,len(array)):
        if isList(array[i]):
            FlattenList(array[i])
        else:
            l.append(array[i])
    return l


    
l = []
print(FlattenList(array))