def common_list(lst1, lst2):
    result=False
    for x in lst1:
        for y in lst2:
            if x == y:
                result=True
                return result
print(common_list([1,2,3,4,5],[6,7,8,9,10]))
print(common_list([1,2,3,4,5],[1,2,3,4,5]))