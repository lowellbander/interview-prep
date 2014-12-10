
def common_k_substring(A, B, k):
    # Figure out if there is any common substring of length at least k.
    # (i.e. any string of length at least k, that is a substring of both A and B)
    # 
    # A="facebook", B="textbook", k=4  ==> true
    # A="facebook", B="textbook", k=5  ==> false
    
    allSubstrings = {}
    
    # O(n), n = A.len(): for looping
    # O(k), inserting into dictionary
    for startingIndex in range(A.len() - k + 1):
        allSubstrings[A[startingIndex:startingIndex + k]] = 0
    
    # allSubstring contains all k length substrings of A
    
    # O(n), n = B.len(): for looping
    # O(k), lookup into dictionary
    for startingIndex in range(B.len() - k + 1):
        if B[startingIndex:startingIndex + k] in allSubstrings:
            return True
            
    return False
    
    # O(k*(A.len() + B.len())
