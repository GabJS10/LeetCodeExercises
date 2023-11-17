"""
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

"""
thoughts

Recorrer cada elemento de la lista original.

En cada pasada, crear dos listas, la de los numeros a la izquierda de i y la de los numeros
a la derecha de i.

luego de tener las dos listas, obtener el producto de ambas (con una funcion auxiliar).

luego multiplicamos los productos y lo que nos de lo añadimos a la lista de "answer" (respuesta)
"""

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i,num in enumerate(nums):
                right = []
                left = []
                if i == 0:
                        right = nums[i+1::]
                elif i==len(nums)-1:
                        left = nums[i-1::-1]
                else:
                        right = nums[i+1::]
                        left = nums[i-1::-1]

                rs = multiplyList(right) * multiplyList(left)

                ans.append(rs)


        return ans

#The productExceptSelf is a solution but is not O(n) 


#This is the correct answer
def OtherSolutionApproach(nums):
       product=1
       right=[]
       left=[]
       ans=[]
       
       for i in range(len(nums)):
                right.append(product)
                product *=nums[i]

       product=1

       for num in reversed(nums):
                left.append(product)
                product *=num

       left=list(reversed(left))

       for i in range(len(nums)):
              ans.append(right[i]*left[i])

       return ans
if __name__ == "__main__":
        print(OtherSolutionApproach([3,4,5,6,7]))