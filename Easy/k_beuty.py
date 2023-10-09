def divisorSubstrings(num, k):
     myNum = str(num)
     count = 0
     for i in range(len(myNum) - k + 1):
          window = myNum[i:i+k]

          window = int(window)

          if window == 0:
               continue

          if num%window == 0:
               count+=1
     
     return count

if __name__ == "__main__":
     print(divisorSubstrings(430043,2))
        