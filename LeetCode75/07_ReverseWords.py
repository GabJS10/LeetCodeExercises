def reverseWords(s):
     """
     :type s: str
     :rtype: str
     """

     arrStr = s.split()

     arrStr.reverse()

     return " ".join(arrStr)

if __name__ == "__main__":
     print(reverseWords("a good   example"))