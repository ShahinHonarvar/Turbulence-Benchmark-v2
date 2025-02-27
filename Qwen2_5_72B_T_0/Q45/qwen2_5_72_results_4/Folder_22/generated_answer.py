from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:7].lower()
    counter = Counter(substring)
    palindromes = set()
    if len(substring) < 2:
        return palindromes
    for length in range(3, 8, 2):
        for char, count in counter.items():
            if count >= length // 2:
                left = char * (length // 2)
                for middle in counter.keys():
                    palindrome = left + middle + left[::-1]
                    palindromes.add(palindrome)
    return palindromes