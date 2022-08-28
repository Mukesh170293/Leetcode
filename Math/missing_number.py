def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_of_nums = 0
    expected = (len(nums) + 1) * len(nums) / 2
    for i in range(len(nums)):
        sum_of_nums += nums[i]
    return expected - sum_of_nums