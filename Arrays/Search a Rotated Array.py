def binary_search_rotated(nums, target):
    start = 0
    end = len(nums) - start - 1
    # if start > end:
    #     return -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1