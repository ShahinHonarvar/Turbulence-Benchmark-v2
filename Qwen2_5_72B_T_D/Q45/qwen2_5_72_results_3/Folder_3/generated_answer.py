from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    counter = Counter(substring)
    palindromes = set()
    for char, count in counter.items():
        if count >= 2:
            for middle in counter.keys():
                palindrome = char + middle + char
                palindromes.add(palindrome)
    return palindromes