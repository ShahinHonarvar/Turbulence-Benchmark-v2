def palindromes_of_specific_lengths(text):
    """
    Returns a set of all palindromes in the given text that meet the following
    requirements:
    1. Only palindromes occurring in the substring from index 32 to index 79, both inclusive, should be considered.
    2. Only palindromes of lengths between 35 to 41 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    substring = text[32:80]
    for i in range(len(substring) - 35):
        for j in range(35, 42):
            window = substring[i:i + j]
            if window == window[::-1] and window.isalpha():
                palindromes.add(window)
    return palindromes