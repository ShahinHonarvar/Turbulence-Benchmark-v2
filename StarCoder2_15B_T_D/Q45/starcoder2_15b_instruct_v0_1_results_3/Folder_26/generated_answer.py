def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 6, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
    """
    palindromes = set()
    letters = [letter for letter in string.lower() if letter.isalpha() and 4 <= string.index(letter) <= 6]
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            palindrome = ''.join(letters[i:i + length])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes