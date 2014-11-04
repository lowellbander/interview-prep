def find_duplicate(nums):
    found = {}
    for num in nums:
    	if num in found:
    		return num
    	else:
    		found[num] = True
    return None

