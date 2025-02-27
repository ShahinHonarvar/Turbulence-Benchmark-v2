from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:7]
    counter = Counter(substring.lower())
    odd_count = sum((1 for count in counter.values() if count % 2 != 0))
    possible = set()
    if odd_count <= 1:
        half_palindrome = ''
        middle = ''
        for char, count in counter.items():
            half_palindrome += char * (count // 2)
            if count % 2 != 0:
                middle = char
        for perm in set((''.join(p) for p in permutations(half_palindrome))):
            palindrome = perm + middle + perm[::-1]
            if len(palindrome) >= 7:
                possible.add(palindrome)
    return possible