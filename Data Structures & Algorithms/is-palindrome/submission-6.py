class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowers = s.lower()
        
        r = len(lowers) -1
        i = 0

        while i < r:
            while i<r and not lowers[i].isalnum():
                i+=1
            while i<r and not lowers[r].isalnum():
                r-=1
                print('alpha r')
                print(r)
            if lowers[i] != lowers[r]:
                return False
            r-=1
            i+=1
        return True    