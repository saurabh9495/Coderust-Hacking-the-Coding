def binary_search(nums,target):
    if not nums:
        return -1
    start = 0
    end = len(nums) - start - 1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
