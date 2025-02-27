def palindromes_between_indices(s: str) -> set:
    """
    Creates all possible palindromes of length >= 3 from the English letters in the given string
    that occur between index 0 and index 6, both inclusive.
    """
    s = s.upper()
    palindromes = set()
    for i in range(len(s)):
        if s[i].isalpha():
            for j in range(i + 1, min(i + 7, len(s))):
                if s[j].isalpha():
                    palindrome = s[i:j + 1]
                    if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes