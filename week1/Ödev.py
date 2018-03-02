import random
arr = [None] * 100
x = range(1, 100)
for i in x:
    arr[i] = i
arr[0]=random.randint(1,99)
print(arr)
random.shuffle(arr)
print(arr)