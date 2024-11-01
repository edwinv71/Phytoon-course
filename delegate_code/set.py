##creation
unique_num2 = set({4,55,66,44,55,66}) #
unique_num2 = set([44,55,66,44,55,66]) #
unique_num2 = set((4,55,66,44,55,66)) #

#sets however DO NOT convert from dictionaries

#most common use case:convert from list and back again to remove duplicates in a list
nums = [44,55,66,44,55,66]
unique_nums5 = set(nums)
unique_nums5_as_list = list(unique_nums5)

##compairing  setss-very powerful for data science
unique_num6 = {55,66,33,22,11}
print(common_values := nums.intersection(unique_num6)) 66,55
print(common_values := nums.difference(unique_num6)) 44
print(common_values := nums.symmetric_difference(unique_num6))

#reflective and no reflective-difference between the caler and the called