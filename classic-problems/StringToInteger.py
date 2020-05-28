
import re

class Solution:
    """Convert a string to an integer.

    Whitespace characters should be removed until first non-whitespace character
    is found. 
    
    Next, and optional plus or minus sign may be found which should then be followed 
    by any number of numerical digits.
    
    The digits should then be converted to and returned as an integer.
    """
    def myAtoi(str) -> int:
        """Strips string of white space characters and searches for strings that may only
        start with 0 or 1 '+' or '-' signs followed by and ending with digits. 
        
        If the pattern is found, returns the integer or the max 
        or min if it exceed 2**31 - 1 or -2**31.
        """
        str = str.strip()
        pattern = r"^[+-]?\d+"
        if re.search(pattern=pattern, string=str):
            num = re.search(pattern=pattern, string=str).group()
            return max(-pow(2, 31), min(pow(2, 31) - 1, int(num)))
        else:
            return 0

    def myAtoi2(str) -> int:
        """Another possible solution similar to above but utilizes if statements to 
        determine which int value to return.
        """
        int_max = 2**31 - 1
        int_min = -2**31
        str = str.strip()
        pattern = re.compile('^[+-]?\d+')
        result = re.search(pattern, str)
        if result:
            num = int(result[0])
            if num > int_max:
                return int_max
            elif num < int_min:
                return int_min
            else:
                return num
        else:
            return 0


if __name__ == '__main__':
    test = Solution()
    result = test.myAtoi(" 42")
    print(result)
