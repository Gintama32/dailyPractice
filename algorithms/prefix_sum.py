arr = [3,4,1,5,7] 
# sum_arr = [3,7,8,13,20]  ans = 13
n = len(arr)
sum_arr = [arr[0]]*n

def prefix_sum():
    for i in range(1,n):
        sum_arr[i] = sum_arr[i-1] + arr[i]
prefix_sum()
print(sum_arr)
def sum_between(i,j):
    if i==0:
        return sum_arr[j]
    sum_btwn = sum_arr[j] - sum_arr[i-1]
    return sum_btwn

print(sum_between(0,4))

