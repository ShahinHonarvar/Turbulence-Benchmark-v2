def palindromes_of_specific_lengths(s: str) -> set:
    """
    Finds the set of all palindromes of lengths between 10 and 50 (both inclusive) in the
    substring from index 10 to 100 (both inclusive) of the given string `s`, where each
    palindrome consists only of English letters and is found in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(10, min(len(s) - 10, 101)):
        for j in range(i + 10, min(i + 51, 101)):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes