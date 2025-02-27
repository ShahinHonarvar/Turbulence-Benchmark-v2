from itertools import permutations
    from collections import Counter

def palindromes_between_indices(text):
    s = text[0:8].lower()
    c = Counter(s)
    center = ''.join([i * (f // 2) for i, f in c.items() if f > 1])
    odd_char = ''.join([i for i, f in c.items() if f % 2 == 1])
    all_perms = set(permutations(''.join(c.elements())))
    palindromes = set()
    for perm in all_perms:
        perm_str = ''.join(perm)
        if len(perm_str) < 5:
            continue
        if center:
            palindrome = perm_str[:len(perm_str) // 2]
            if len(perm_str) % 2 == 1:
                palindrome += odd_char[0]
            palindrome += palindrome[::-1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
        else:
            palindrome = ''.join(sorted(perm_str))
            palindrome += palindrome[::-1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes