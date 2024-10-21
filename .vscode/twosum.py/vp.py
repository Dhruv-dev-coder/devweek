class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if "(" in a:
            if ")" in a:
                return True
            else:
                return False   
        if "{" in a:
            if "}" in a:
                return True
            else:
                return False  
        if "[" in a:
            if "]" in a:
               return True
            else:
                return False
a=str(input("Enter the paranthesis:"))  
sol = Solution()
print(sol.isValid(a))