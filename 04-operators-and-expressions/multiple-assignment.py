# list
my_nums = [1,2,3]
# first, second, third = my_nums[0], my_nums[1], my_nums[2]
first, second = my_nums[0], my_nums[1]
num1 = my_nums[0]
first_list, second_list, third_list= my_nums#see separate file
# first_list, second_list, third_list, extra_element = my_nums#see separate file
# first_list, second_list = my_nums#ValueError: too many values to unpack (expected 2)
print(first_list)
print(second_list)
print(third_list)
# print(extra_element) #ValueError: not enough values to unpack (expected 4, got 3)
print(first, second)#1, 2
# using indices, the number of elements we unpack has more control
# without inices, the numebr of elements we unpack must be the same as is in the data