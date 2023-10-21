import math

def reorderSpaces(text):
        """
        :type text: str
        :rtype: str
        """
        result = None
        textSplit = text.split()
        spaces = text.count(" ")

        extra_space = spaces / (len(textSplit)-1)
        if extra_space>len(textSplit):
                extra_space_round = round(extra_space)
                additional = extra_space_round-len(textSplit)
                df = math.floor(extra_space)
                result = (" "*df).join(textSplit)
                result = result.ljust(len(result)+additional)
        else:
                df = math.floor(extra_space)
                result = (" "*df).join(textSplit)      

        
        return result       
        


if __name__ == "__main__":
        print(reorderSpaces("  hello"))