def palindromes_between_indices(string):
    """
    <Write a function called 'palindromes_between_indices' that takes one argument, which is a string. The given string may consist of any character. The function should return the set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 9, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.>
    """
    string = string.lower()
    palindromes = set()
    for i in range(4, 10):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes