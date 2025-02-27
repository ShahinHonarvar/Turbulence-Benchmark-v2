def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of length at least 3 that can be created from
    any possible arrangement of the English letters in the given string that occur
    between indices 5 and 8, both inclusive. If no such palindromes can be created,
    returns an empty set.
    """
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes