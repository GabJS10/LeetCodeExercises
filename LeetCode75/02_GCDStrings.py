import math

def gcdOfStrings(str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 == str2 + str1:
                str3 = str1 + str2 
                return str3[:math.gcd(len(str1),len(str2))]
        
        return ""

if __name__ == "__main__":
        print(gcdOfStrings("LEET","CODE"))