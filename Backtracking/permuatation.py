def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    l = []
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    for i in range(len(nums)):
        m = nums[i]
        remLst = nums[:i] + nums[i + 1:]
        for p in permute(remLst):
            l.append([m] + p)
    return l