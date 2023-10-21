def leftRightDifference(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        if len(nums)>1:
               leftSum = []
               rightSum = []
               sumLeft = 0
               sumRight=0
               for i in range(len(nums)-1):
                    if i==0:
                         leftSum.append(0)

                    sumLeft=nums[i] + sumLeft
                    leftSum.append(sumLeft)

        
               for i in range(len(nums)-1,0,-1):
                    if i == len(nums)-1:
                              rightSum.append(0)
                         
                    sumRight=nums[i] + sumRight
                    rightSum.append(sumRight)  
               else:
                    rightSum.reverse()

               for i in range(len(nums)):
                    answer.append(abs(leftSum[i] - rightSum[i]))

        return answer or [0]              
 
if __name__ == "__main__":
     print(leftRightDifference([10,4,8,3]))