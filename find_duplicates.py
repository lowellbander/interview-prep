"""find the duplicates in a list in constant time"""

def find_duplicates(nums):
    """find the duplicates in a list in constant time"""
    found = {}
    for num in nums:
        if num in found:
            found[num] += 1
        else:
            found[num] = 1
    return [num for num in found if found[num] > 1]
