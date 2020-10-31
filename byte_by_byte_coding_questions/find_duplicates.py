def dups(arr):
    # Return if empty or single item
    if len(arr) <= 1:
       return []

    temp_dict ={}
    set_x = set()
    n =  len(arr)

    for i in range(0,n):
        val = arr[i]
        if val in temp_dict:
            temp_dict[val] = int(temp_dict.get(val)) + 1
        else:
            temp_dict[val] = 1   

        if int(temp_dict.get(val)) >= 2:
            set_x.add(val)

    return list(set_x)    




x = dups([])
print(x)

x= dups([1])
print(x)

x = dups([1,2,3])
print(x)

x = dups([1,2,2])
print(x)

x = dups([3,3,3,3])
print(x)

x = dups([2,1,2,1,3,3,3])
print(x)