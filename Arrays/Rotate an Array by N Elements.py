def reverse_array(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1    

def rotate_array(nums,n):
    n = n % len(nums)
    if n < 0:
        n+= len(nums)
    reverse_array(nums,0,len(nums)-1)
    reverse_array(nums,0,n-1)
    reverse_array(nums,n,len(nums)-1)