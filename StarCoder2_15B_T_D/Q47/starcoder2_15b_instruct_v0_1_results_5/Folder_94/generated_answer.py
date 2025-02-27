def palindromes_of_specific_lengths(string):
    """
    Returns a set of all palindromes in a given string with specific lengths and
    index range. Only palindromes of lengths between 45 to 51 (both inclusive)
    should be considered. Only palindromes occurring in the substring from index
    40 to index 94, both inclusive, should be considered. Each palindrome should
    only consist of English letters. If no such palindrome with the length
    specified occurs in the specified index range, the function should return an
    empty set. The function should find the palindromes in a case-insensitive
    manner.
    """
    palindromes = set()
    substring = string[40:95]
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes