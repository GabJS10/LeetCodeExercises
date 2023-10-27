def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
          You have a long flowerbed in which some of the plots are planted,
          and some are not. However, flowers cannot be planted in adjacent plots.
          Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
          and an integer n, return true if n new flowers can be planted in the flowerbed 
          without violating the no-adjacent-flowers rule and false otherwise.

          Example 1:
          Input: flowerbed = [1,0,0,0,1], n = 1
          Output: true
          Example 2:

          Input: flowerbed = [1,0,0,0,1], n = 2
          Output: false

          Necesito recorrer el array de flowerbed
          1. verificar si hay una flor plantada (1) en este caso pasaremos a la siguiente posicion
          2. en caso de ser 0 (no hay flor) verificaremos si hay flores adyacentes flowerbed[index-1] y 
          flowerbed[index+1]
          3. SI ambos valores adyacentes son 0 entonces plantaremons una flor (cambiamos el valor actual) 
          e incrementamos uno la variable contadora
          4. retornar si el valor de la variable es igual al numero e flores que nos piden plantar

        """

        if n==0:
               return True

        if len(flowerbed) == 1:
               if flowerbed[0] == 0:
                      return True

               if flowerbed[0] == 1:
                      return False

        count=0
        for index,flower in enumerate(flowerbed):
                if flower==1:
                        continue
                
                if index==0:
                        if flowerbed[index+1]==0:
                         count+=1
                         flowerbed[index] = 1
                         continue
                        continue
                        
                if index==len(flowerbed)-1:
                       if flowerbed[index-1]==0:
                         count+=1
                       continue
                        
                if flowerbed[index+1]==0 and flowerbed[index-1]==0:
                         count+=1
                         flowerbed[index] = 1
                         continue
                
                
        return True if count >= n else False
                       

                


if __name__ == "__main__":
        print(canPlaceFlowers([1,0,0,0,1,0,0],2))
        