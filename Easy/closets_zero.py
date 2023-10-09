
def findClosestNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        list_negatives_abs = []
        list_positivs = []

        for num in nums:
                if num < 0:
                        list_negatives_abs.append(num*-1)
                else:
                        list_positivs.append(num)       

          
        list_negatives_abs.sort()
        list_positivs.sort()

        if len(list_negatives_abs) == 0:
                return list_positivs[0]
        
        if len(list_positivs) == 0:
                return list_negatives_abs[0]*-1

        if list_negatives_abs[0] < list_positivs[0]:
                return list_negatives_abs[0]*-1
        elif list_negatives_abs[0] > list_positivs[0] or list_negatives_abs[0] == list_positivs[0]:
                return list_positivs[0]
  

if __name__ == "__main__":
        num = findClosestNumber([-100000,-100000])
        print(num)