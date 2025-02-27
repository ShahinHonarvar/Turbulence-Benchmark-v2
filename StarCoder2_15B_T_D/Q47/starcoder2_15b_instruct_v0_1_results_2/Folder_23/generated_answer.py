import re

def palindromes_of_specific_lengths(s):
    """
    Finds palindromes in a given string's' that meet the following criteria:
    1. Only palindromes occurring in the substring from index 23 to index 94, both inclusive, should be considered.
    2. Only palindromes of lengths between 17 to 55 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    substring = s[23:95]
    pattern = '[a-zA-Z]{' + str(17) + ',' + str(55) + '}'
    matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes