from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:7]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]
    palindromes = set()
    if len(odd_chars) <= 1:
        half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
        possible_center = odd_chars[0] if odd_chars else ''
        for perm in set([''.join(p) for p in permutations(half_palindrome + possible_center + half_palindrome[::-1], 7)]):
            palindromes.add(perm)
    return palindromes