lists = [1, 2, 3, 5 ]

# reading list
print(lists[0])



if 1 in lists: print(True) # this search item in the list called contained methods in under the hood it uses linear search



for n in lists:

    if n == 1:
        print(True)
        break


lists.append(5) # every append operators add element to list when certained memory space already allocated
# so 0, 4, 8, 16, 35, 46 etc these memory filled during append operators the system itself called listresize opertor to reallocate the 
# memory