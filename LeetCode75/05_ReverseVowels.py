def reverseVowels(s):
        """

        :type s: str
        :rtype: str

     Given a string s, reverse only all the vowels in the string and return it.

     The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
     more than once.

     Example 1:
     Input: s = "hello"
     Output: "holle"

     Example 2:
     Input: s = "leetcode"
     Output: "leotcede"
     

     Constraints:
     1 <= s.length <= 3 * 105
     s consist of printable ASCII characters.


     1.crear array de vowels (vocales) y variable J que va a llevar el indice del ciclo que 
      recorrera el array al reves (inicialmente estara al final de la cadena)
     2. recorrer string
     3. si encontramos una vocal entonces iniciaremos un recorrido desde la ultima vocal mientras que
     j sea mayor que i
     4.si encontramos una vocal en el recorrido al reves del ciclo, entonces intercambiamos la vocal actual i
     con la vocal actual inversa j y decrementamos j para la siguiente vez no tener en cuenta esta vocal
        """

        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        j = len(s)-1
        s_list = list(s)

        for i in range(len(s_list)):
                if s_list[i] in vowels:
                        while i<j:
                                if s_list[j] in vowels:
                                        aux = s_list[j]
                                        s_list[j] = s_list[i]
                                        s_list[i] = aux
                                        j-=1
                                        break
                                j-=1
        return "".join(s_list)
if __name__ == "__main__":
        print(reverseVowels("leetcode"))

        