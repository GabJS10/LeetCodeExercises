def isLongPressedName(name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        """
        isOk=True
        beforeChar = None
        for i, c in enumerate(name):
                

                if name[i] != typed[i]:
                        
                        if i == 0:
                                print("entro")
                                isOk=False
                                break
                        
                        if beforeChar and typed[i] != beforeChar:
                                isOk=False
                                break
                
                beforeChar = c

                if typed.count(c) >= name.count(c):
                          continue
                isOk=False

        return isOk
        """


        i, j = 0, 0  # Inicializa los índices para name y typed

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1

     # Verifica si se han recorrido completamente ambos arreglos
        return i == len(name)

if __name__ == "__main__":
        print(isLongPressedName("vtkgn","vttkgnn"))
        