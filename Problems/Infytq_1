def reach(n):

    '''
        Function for finding the reachable numbers
    '''
    def filter_0(value):
        
        '''
            function for adding 1 and popping zeros from the end
        '''
        value += 1
        value = str(value)
        while value[-1] == '0':
            value = value[:-1]
        return int(value)

    dict1 = {}
    dict1[n] = 0
    while True:
        n = filter_0(n)
        if n in dict1:
            break;
        else:
            dict1[n] = 0

    return len(dict1)
