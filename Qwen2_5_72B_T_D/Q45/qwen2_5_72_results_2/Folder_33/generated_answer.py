from collections import Counter

def palindromes_between_indices(s):
    s_subset = s[7:10]
    counter = Counter(s_subset.lower())
    even_chars = [char for char, count in counter.items() if count % 2 == 0 for _ in range(count // 2)]
    odd_chars = [char for char, count in counter.items() if count % 2 == 1]
    if len(odd_chars) > 1:
        return set()
    middle = odd_chars[0] if odd_chars else ''
    half_palindrome = ''.join(even_chars)
    palindromes = set()
    for i in range(len(half_palindrome) + 1):
        for j in range(len(middle) + 1):
            palindrome = half_palindrome[:i] + middle[:j] + middle[j] + half_palindrome[i:][::-1]
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes