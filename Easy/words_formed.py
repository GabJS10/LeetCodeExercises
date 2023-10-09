def countCharacters(words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        """
        ans = 0
        for word in words: 
            for char in word: 
                if word.count(char) > chars.count(char):  break
            else: ans += len(word)
        return ans
        """

        sum = 0
        for word in words:
                count = 0
                chars_list = list(chars)
                for i in range(len(word)):
                        if word[i] in chars_list:
                                count+=1
                                chars_list.remove(word[i])
                if count==len(word):
                        sum+=len(word)

        return sum                
                


if __name__ == "__main__":
        print(countCharacters(["hello","world","leetcode"],"welldonehoneyr"))      