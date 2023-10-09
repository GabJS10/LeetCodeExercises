import random


def removeAnagrams(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words_without_anagrams = [words[0]]

        for i in range(1,len(words)):
               word_arr = list(words[i])
               word_before_arr = list(words[i-1])
               
               word_arr.sort()
               word_before_arr.sort()

               if word_arr != word_before_arr:
                      words_without_anagrams.append(words[i])

        return words_without_anagrams            

if __name__ == "__main__":
     myList = removeAnagrams(["abba","baba","bbaa","cd","cd"])
     print(myList)