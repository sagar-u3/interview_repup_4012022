def max_points(k,costs):
    i=0
    skip = 0
    while i<len(costs) and (k>=costs[i] or k>=skip<costs[i]):
        if costs[i]>skip:
            k-=skip
            skip=costs[i]
        else:
            k-=costs[i]
        i=i+1
    return i

if __name__=='__main__':
    k = int(input('Wallet Balance:' ))
    n = int(input('Number of Levels: '))
    costs = [int(input(f'Cost {i+1}: ')) for i in range(n)] 
    print('Maximum possible score:',max_points(k,costs))