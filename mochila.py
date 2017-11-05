capacity = 0
weight = []
value = []
memo = []
def solve(item, val, cap):
    global weight, value, memo
    if(item < len(weight) and cap>=0 and memo[cap][item]>0):
        return memo[cap][item]
    if(cap<0):
        return 0
    if(item>=len(weight)):
        return val
    memo[cap][item] = max(solve(item+1,val+value[item],cap-weight[item]),solve(item+1,val,cap))
    return memo[cap][item]

def main():
    global capacity,memo
    with open("mochila.txt") as f:
        i = 0
        for line in f:
            if(i == 0):
                capacity = int(line)
            else:
                temp = line.rstrip("\n")
                for num in temp.split(","):
                    if(i == 1):
                        weight.append(int(num))
                    else:
                        value.append(int(num))
            i+=1
    for i in range(capacity+1):
        memo.append([])
        for j in range(len(weight)):
            memo[i].append([])
            memo[i][j] = 0
    print(solve(0,0,capacity))
    aux = 0
    items = []
    for i in range(1,len(weight)):
        if(memo[-1][aux]!=memo[-1][i] and capacity>0):
            items.append(i)
            capacity-=weight[aux]
            aux = i
    if(capacity>0 and weight[-1]<capacity):
        items.append(len(weight))
    print(items)

if __name__ == '__main__':
    main()
