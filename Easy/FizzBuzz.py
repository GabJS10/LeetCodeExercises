class Solution(object):
    def fizzBuzz(self, n):
        listOut = []
        for num in range(1,n+1):
            if num % 3 == 0 and num % 15 == 0:
                listOut.append("FizzBuzz")
            elif num % 3 == 0:
                listOut.append("Fizz")
            elif num % 5 == 0:
                listOut.append("Buzz")
            else:
                listOut.append(str(num))

        return listOut




if __name__ == "__main__":
     s = Solution()
     out = s.fizzBuzz(15)
     print(out)