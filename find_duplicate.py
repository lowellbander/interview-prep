"""find the duplicates in a list in constant time"""

def find_duplicate(nums):
    """find the duplicates in a list in constant time"""
    found = {}
    for num in nums:
        if num in found:
            return num
        else:
            found[num] = True
    return None

