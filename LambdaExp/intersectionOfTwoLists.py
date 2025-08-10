# find common elements in two lists

# using for loop
def intersection(lst1,lst2):
    lst1.sort()
    lst2.sort()
    commelements= []

    for i1 in lst1:
        if i1 in lst2 and i1 not in commelements:
            commelements.append(i1)
    return commelements


list1 =[3,5,6,7,2,56,9,23]
list2 = [3,5,6,24,7,55,8,2]

# print(intersection(list1,list2))

# using list comprehension
def intersection_comp(lst1,lst2):
    return [item for item in lst1 if item in lst2]

print(intersection_comp(list1,list2))
