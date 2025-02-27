from itertools import product

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = 44
    palindromes = set()
    first_half_length = (length + 1) // 2
    for indices in product(range(len(s) - first_half_length + 1), repeat=first_half_length):
        half = ''.join((s[i] for i in indices))
        if len(half) < first_half_length:
            break
        full = half + half[::-1][len(half) % 2:]
        if full.count(' ') > 0:
            continue
        palindromes.add(full)
    return palindromes