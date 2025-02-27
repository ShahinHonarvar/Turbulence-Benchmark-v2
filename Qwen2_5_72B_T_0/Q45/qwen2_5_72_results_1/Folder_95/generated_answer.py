from collections import Counter

def palindromes_between_indices(s):
    substring = s[7:9].lower()
    counter = Counter(substring)
    palindromes = set()
    for length in range(3, 10, 2):
        for char, count in counter.items():
            if count >= length // 2:
                left = char * (length // 2)
                for middle in counter.keys():
                    palindrome = left + middle + left[::-1]
                    palindromes.add(palindrome)
    return palindromes