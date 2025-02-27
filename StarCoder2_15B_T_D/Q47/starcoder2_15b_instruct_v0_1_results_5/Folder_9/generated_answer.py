import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    1. Only palindromes occurring in the substring from index 0 to index 300, both inclusive, should be considered.
    2. Only palindromes of lengths between 50 to 60 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    substring = string[:301]
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(60) + '}'
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            match = re.search(pattern, substring[i:j])
            if match:
                palindrome = match.group().lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes