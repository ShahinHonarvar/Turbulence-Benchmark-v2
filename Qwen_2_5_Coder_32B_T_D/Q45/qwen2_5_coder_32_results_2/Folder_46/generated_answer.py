from collections import Counter
    import itertools

def palindromes_between_indices(s):
    s = s[4:10].lower()
    char_count = Counter(s)
    usable_chars = ''.join([char * (count // 2) for char, count in char_count.items() if char.isalpha()])
    palindromes = set()
    for i in range(1, len(usable_chars) + 1):
        for half in itertools.permutations(usable_chars, i):
            half_str = ''.join(half)
            middle = '' if len(half_str) * 2 < 6 else max((char for char, count in char_count.items() if count % 2 == 1 and char.isalpha()), default='')
            palindrome = half_str + middle + half_str[::-1]
            if len(palindrome) >= 6:
                palindromes.add(palindrome)
    return palindromes