
def cumulative_sum(lst):
    sum=0
    cumlst=[]
    for itm in lst:
        sum = sum + itm
        cumlst.append(sum)

    print(cumlst)
    return sum

list1= [22,4,5,6,77,2]
cumsum = cumulative_sum(list1)
print(cumsum)