def oddString(words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        abecedario = list("abcdefghijklmnopqrstuvwxyz")
        
        listaOut = []

        for i in range(len(words)):
                list_for_word = []
                word = list(words[i])
                for j in range(len(word)):
                        if j+1<len(word):
                              list_for_word.append(abecedario.index(word[j])-abecedario.index(word[j+1]))
                listaOut.append(list_for_word)
                


        for i in range(len(listaOut)):
          is_unique = True
          for j in range(len(listaOut)):
               if i != j and listaOut[i] == listaOut[j]:
                    is_unique = False
                    break

          if is_unique:
               return words[i]

        return None
        


        

if __name__ == "__main__":
        print(oddString(["adc","wzy","abc"]))