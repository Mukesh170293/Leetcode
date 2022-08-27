def contains_duplicate_ii(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # for i, el in enumerate(nums):
    #     if el in nums[i + 1:i + k + 1]:
    #         return True
    # return False
    seen = {}
    for index, val in enumerate(nums):
        if seen.get(val, -1) != -1 and index - seen[val] <= k:
            return True
        else:
            seen[val] = index
    return False
