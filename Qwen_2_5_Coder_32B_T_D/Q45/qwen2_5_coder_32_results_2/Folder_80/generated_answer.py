from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    count = Counter(letters)
    odd_count = sum((1 for c in count if count[c] % 2))
    half_length = len(letters) // 2 + (1 if odd_count > 1 else 0)
    half_palindrome_set = set()
    result = set()
    if len(letters) < 7:
        return result
    if odd_count > 1:
        for c in count:
            if count[c] % 2 == 1:
                odd_char = c
                count[c] -= 1
                break

    def permute_half(current, remaining):
        if len(current) == half_length:
            half_palindrome_set.add(''.join(current))
            return
        for char in set(remaining):
            if remaining.count(char) > 1:
                permute_half(current + [char], [c for c in remaining if c != char])
    permute_half([], letters)
    if odd_count > 1:
        for half in half_palindrome_set:
            result.add(half + odd_char + half[::-1])
    else:
        for half in half_palindrome_set:
            result.add(half + half[::-1])
    return result