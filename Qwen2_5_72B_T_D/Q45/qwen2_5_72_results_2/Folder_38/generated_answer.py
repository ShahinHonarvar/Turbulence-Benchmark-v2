from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1 or len(substring) < 5:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in char_count.items()))
    permutations = set([''.join(p) for p in set(itertools.permutations(half_palindrome))])
    palindromes = {p + (odd_chars[0] if odd_chars else '') + p[::-1] for p in permutations if len(p + (odd_chars[0] if odd_chars else '') + p[::-1]) >= 5}
    return palindromes