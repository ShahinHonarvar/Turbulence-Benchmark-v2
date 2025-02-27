from collections import Counter
        from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    counter = Counter(substring)
    middle_chars = [char for char, count in counter.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    results = set()
    if len(middle_chars) <= 1 and len(half_palindrome) >= 3:
        for perm in set(permutations(half_palindrome)):
            candidate = ''.join(perm)
            if middle_chars:
                palindrome = candidate + middle_chars[0] + candidate[::-1]
            else:
                palindrome = candidate + candidate[::-1]
            if len(palindrome) >= 6:
                results.add(palindrome)
    return results