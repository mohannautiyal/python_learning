# Find element with max freq in list

list1 = [22,3,5,6,22,2,4,54,4,22,4,22]


def findmaxfeq(lst):
    cnt = 0
    maxfreq = 0
    maxfeqitm=0
    for itm in lst:
        cnt = lst.count(itm)
        print("Freq of ",itm, " is ",cnt)
        if cnt > maxfreq:
            maxfreq =cnt
            maxfeqitm =itm
        # print(itm,maxfreq,maxfeqitm)

    return maxfeqitm

print("Item with max frequency is " ,findmaxfeq(list1))


