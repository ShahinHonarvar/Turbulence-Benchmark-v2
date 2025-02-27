from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:10]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in counter.items()))
    palindromes = set()
    for i in range(len(half_palindrome) + 1):
        for char in odd_chars:
            palindrome = half_palindrome[:i] + char + half_palindrome[i:]
            if len(palindrome) >= 7:
                palindromes.add(palindrome + palindrome[::-1])
    return palindromes