def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        tam = len(word1) if len(word1)>len(word2) else len(word2)
        ans=""
        for i in range(tam):
                if i>=len(word1) and i<len(word2):
                        ans+=word2[i]
                elif i>=len(word2) and i<len(word1):
                        ans+=word1[i]
                else:
                        ans+=word1[i]
                        ans+=word2[i]

        return ans

if __name__ == "__main__":
        print(mergeAlternately("abcd","pq"))