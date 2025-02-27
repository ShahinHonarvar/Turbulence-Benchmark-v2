def palindromes_of_specific_lengths(string):
    """
    Finds all palindromes in a given string that satisfy the following conditions:
    1. Only palindromes occurring in the substring from index 34 to index 90, both inclusive, should be considered.
    2. Only palindromes of lengths between 14 to 39 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    substring = string[34:91]
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if window.isalpha():
                    palindromes.add(window)
    return palindromes