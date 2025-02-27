from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub_str = s[7:10].lower()
    unique_chars = sorted(set(sub_str))
    min_len = 4
    palindromes = set()
    for p in range(min_len, len(unique_chars) + 1):
        for perm in permutations(unique_chars, p):
            perm_str = ''.join(perm)
            for i in range(len(perm_str) // 2 + 1):
                left = perm_str[:i]
                right = perm_str[-i:]
                if left == right[::-1]:
                    palindromes.add(left + right)
    return palindromes