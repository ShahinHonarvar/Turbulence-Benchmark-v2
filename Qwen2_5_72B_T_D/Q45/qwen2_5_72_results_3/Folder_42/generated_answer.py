from collections import Counter

def palindromes_between_indices(s):
    substring = s[6:10]
    char_count = Counter(substring.lower())
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    center = ''
    if odd_chars:
        center = odd_chars[0]
        char_count[center] -= 1
    half_palindrome = ''.join([char * (count // 2) for char, count in char_count.items()])
    palindromes = set()
    if len(half_palindrome) + len(center) >= 3:
        for perm in set([''.join(p) for p in itertools.permutations(half_palindrome)]):
            palindrome = perm + center + perm[::-1]
            palindromes.add(palindrome)
    return palindromes