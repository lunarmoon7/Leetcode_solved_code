# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0
        
        for i in range(1, n):
            if knows(i, celeb) and not knows(celeb, i):
                continue
            else:
                celeb = i
        for j in range(celeb):
            if not knows(j, celeb) or knows(celeb, j):
                return -1
        return celeb
                        
                    
            
#             candidate = 0
#         for i in range(1, n):
#             if knows(i, candidate) and not knows(candidate, i):
#                 continue
#             else:
#                 candidate = i
#         for j in range(candidate):
#             if not knows(j, candidate) or knows(candidate, j):
#                 return -1
#         return candidate
                    