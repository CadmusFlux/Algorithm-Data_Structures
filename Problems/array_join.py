
def myfunc(list1,list2):

    len1 = len(list1)
    len2 = len(list2)

    if len1>len2:
        length = len1
    elif len1<len2:
        length = len2
    else:
        length = len1

    output = []

    for i in range(length):

        if i < len1 and i < len2:
            output.append(list1[i])
            output.append(list2[i])
        elif i>= len1 :
            output.extend(list2[i:])
            break
        elif i >= len2:
            output.extend(list1[i:])
            break
        else:
            break

    return output
