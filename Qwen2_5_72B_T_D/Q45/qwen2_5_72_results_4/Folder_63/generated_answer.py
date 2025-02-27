from collections import Counter

def palindromes_between_indices(s):
    substring = s[:4]
    char_count = Counter(substring)
    palindromes = set()
    for first_last in char_count:
        for middle in char_count:
            if first_last.lower() == first_last.upper() and middle.lower() == middle.upper():
                continue
            if char_count[first_last] >= 2 and first_last.lower() == first_last.upper() or char_count[first_last] >= 2:
                palindrome = first_last + middle + first_last
                palindromes.add(palindrome.lower())
    return palindromes