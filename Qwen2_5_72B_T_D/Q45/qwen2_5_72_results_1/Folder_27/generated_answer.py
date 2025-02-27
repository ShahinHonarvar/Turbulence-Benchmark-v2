from collections import Counter
        from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    char_counts = Counter(substring)
    even_chars = [char for char, count in char_counts.items() if count % 2 == 0 for _ in range(count // 2)]
    odd_chars = [char for char, count in char_counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    palindromes = set()
    if len(odd_chars) == 1:
        middle_char = odd_chars[0]
    else:
        middle_char = ''
    for length in range(6, 13, 2):
        if len(even_chars) * 2 + len(middle_char) < length:
            continue
        for perm in set(permutations(even_chars, length // 2)):
            palindrome = ''.join(perm) + middle_char + ''.join(perm[::-1])
            palindromes.add(palindrome)
    return palindromes