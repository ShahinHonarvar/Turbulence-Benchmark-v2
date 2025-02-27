from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.lower() in string.ascii_lowercase, s[2:10])).lower()
    count = Counter(letters)
    usable_letters = ''.join([char * (count[char] // 2) for char in count])

    def is_palindrome(p):
        return p == p[::-1]
    palindromes = set()
    for perm in permutations(usable_letters):
        half = ''.join(perm)
        full = half + (max((char for char, cnt in count.items() if cnt % 2 == 1), default='') + half[::-1])
        if len(full) >= 6:
            palindromes.add(full)
    return palindromes