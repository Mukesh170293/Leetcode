def isPowerOfTwo( n):
    """
    :type n: int
    :rtype: bool
    """
    return True if n in {2 ** x for x in range(32)} else False
