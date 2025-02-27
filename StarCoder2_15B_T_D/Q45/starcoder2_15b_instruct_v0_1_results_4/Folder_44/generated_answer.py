def palindromes_between_indices(string):
    """
    This function takes a string as an argument and returns a set of all palindromes of length 3 or more that can be formed from any possible arrangement of the English letters in the given string that occur between indices 2 and 7, both inclusive.
    """
    string = string.lower()
    palindromes = set()
    for i in range(2, len(string) - 1):
        for j in range(i + 1, len(string)):
            for k in range(j + 1, min(j + 4, len(string))):
                palindrome = string[i:k + 1]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes