from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:5]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    half_palindrome = ''
    center = ''
    for letter, count in letter_counts.items():
        half_palindrome += letter * (count // 2)
        if count % 2 != 0 and center == '':
            center = letter
    results = set()
    if len(half_palindrome) == 0:
        return results
    for i in range(len(half_palindrome) + 1):
        for j in range(len(half_palindrome), i - 1, -1):
            if j - i >= 2:
                candidate = half_palindrome[i:j]
                palindrome = candidate + center + candidate[::-1]
                if len(palindrome) >= 5:
                    results.add(palindrome)
    return results