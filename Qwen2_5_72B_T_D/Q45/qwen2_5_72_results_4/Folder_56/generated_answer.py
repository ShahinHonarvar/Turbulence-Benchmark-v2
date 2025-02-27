from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    counter = Counter(substring)
    center = ''
    half_palindrome = ''
    for char, count in counter.items():
        half_palindrome += char * (count // 2)
        if count % 2 == 1 and (not center):
            center = char
    possible_palindromes = set()
    if len(half_palindrome) * 2 + len(center) >= 5:
        for perm in set((''.join(p) for p in itertools.permutations(half_palindrome))):
            palindrome = perm + center + perm[::-1]
            if len(palindrome) >= 5:
                possible_palindromes.add(palindrome)
    return possible_palindromes