def palindromes_between_indices(s):
    """
    Finds all palindromes of length at least 4 that can be formed from the English letters
    in the given string `s` that occur between indices 0 and 7, both inclusive.
    """
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindrome = ''.join(letters[i:j + 1]).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes