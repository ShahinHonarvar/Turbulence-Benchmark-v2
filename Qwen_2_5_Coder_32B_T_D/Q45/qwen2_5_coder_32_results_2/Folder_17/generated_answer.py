from collections import Counter
    import itertools

def palindromes_between_indices(s):
    t = s[2:7].lower()
    c = Counter(t)
    letters = ''.join(c.keys())
    palindromes = set()
    for length in range(4, 8):
        for comb in itertools.combinations_with_replacement(letters, (length + 1) // 2):
            half = ''.join(comb)
            if len(half) * 2 - (length % 2 == 1) <= length:
                count_half = Counter(half)
                for k in count_half:
                    if count_half[k] > c[k]:
                        break
                else:
                    if length % 2 == 0:
                        palindrome = half + half[::-1]
                    else:
                        palindrome = half + half[-2::-1]
                    palindromes.add(palindrome)
    return palindromes