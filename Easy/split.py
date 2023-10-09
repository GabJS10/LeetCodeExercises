def splitWordsBySeparator(words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """

        listOut = []
        for word in words:
                #f = filter(None, word.split(separator))
                listOut.extend(list(filter(None, word.split(separator))))

        return listOut

if __name__ == "__main__":
        print(splitWordsBySeparator(["one.two.three","four.five","six"],"."))