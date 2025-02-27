from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:3].lower()
    counter = Counter(substring)
    result = set()
    for char, count in counter.items():
        if count >= 2:
            for middle_char in counter:
                if counter[middle_char] > 0:
                    palindrome = char + middle_char + char
                    result.add(palindrome)
    return result