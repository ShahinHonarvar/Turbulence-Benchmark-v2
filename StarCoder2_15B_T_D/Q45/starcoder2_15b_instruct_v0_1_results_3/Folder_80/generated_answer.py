def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of length 7 or more that can be formed from the
    English letters in the given string that occur between indices 3 and 8, both inclusive.
    """
    letters = [c for c in string[3:9] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters)):
            palindrome = ''.join(letters[i:j + 1]).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes