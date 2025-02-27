from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:7]
    counter = Counter(substring.lower())
    odd_counts = [char for char, count in counter.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    else:
        half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
        palindromes = set()
        for i in range(len(half_palindrome) + 1):
            for char in odd_counts:
                palindrome = half_palindrome[:i] + char + half_palindrome[i:]
                palindromes.add(palindrome + palindrome[::-1])
        return {palindrome for palindrome in palindromes if len(palindrome) >= 3}