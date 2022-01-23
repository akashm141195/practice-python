# Find which num has max occurences in the list without any dictionary or inbuilt functions

num_list=[1,2,5,7,3,2,6,2,7,2,6,8,3,7,8,6,2,4,4,4,4,4,4]

last_count=-1
for num in num_list:
    count=0
    for idx in range(len(num_list)):
        if num == num_list[idx]:
            count+=1
        if last_count<count:
            last_count=count
            value=num
print(f"Number {value} has max occurences")


##what if two numbers have same occurences?