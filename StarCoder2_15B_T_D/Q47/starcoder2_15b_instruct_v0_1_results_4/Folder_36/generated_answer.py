def palindromes_of_specific_lengths(input_string):
    """
    This function takes a string as input and returns a set of palindromes that satisfy the following criteria:
    1. Only palindromes occurring in the substring from index 124 to 283, both inclusive, should be considered.
    2. Only palindromes of lengths between 115 to 134 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    substring = input_string[124:284]
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes