def palindromes_between_indices(s):
    """
    Given a string, returns the set of all palindromes of length at least 6
    that can be formed from any possible arrangement of the English letters
    in the given string that occur between indices 0 and 6, both inclusive.
    """
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 6, len(letters)):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes