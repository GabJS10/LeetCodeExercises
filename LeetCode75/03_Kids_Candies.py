def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxcandie = max(candies)

        return [candie+extraCandies>=maxcandie for candie in candies]


if __name__ == "__main__":
        print(kidsWithCandies([2,8,7],1))