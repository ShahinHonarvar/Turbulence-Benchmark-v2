def palindromes_of_specific_lengths(string):
    """
    Finds the set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 0 to index 5, both inclusive, should be considered.
    2. Only palindromes of lengths between 3 to 5 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    substring = string[0:6].lower()
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            substring_window = substring[i:i + length]
            reversed_substring_window = substring_window[::-1]
            if substring_window == reversed_substring_window and substring_window.isalpha():
                palindromes.add(substring_window)
    return palindromes