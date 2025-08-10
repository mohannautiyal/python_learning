 # remove duplicates from a lst using set

def removeDups(lst):
    uniqueset =set()
    uniquelst =[]
    for itm in lst:
        if itm not in uniqueset:
            uniquelst.append(itm)
        uniqueset.add(itm)

    return uniquelst

# remove dups without using set
def removeDup(lst):
    uniquelst =[]

    for itm in lst:
        if itm not in uniquelst:
            uniquelst.append(itm)
    return uniquelst


listFruits = ["Apple","Banana","Grapes","Mango","Grapes","Apple"]

print(removeDups(listFruits))
print(removeDup(listFruits))
