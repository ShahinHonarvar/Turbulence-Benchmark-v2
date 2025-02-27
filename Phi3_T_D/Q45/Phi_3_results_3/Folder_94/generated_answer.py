from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    start, end = (3, 4)
    part = s[start:end + 1]
    letters = ''.join(sorted(set(part.lower()), key=lambda c: -part.lower().count(c)))
    palindromes = set()
    for perm in permutations(string.ascii_lowercase, len(letters)):
        s_perm = ''.join(perm)[:len(part)]
        if is_palindrome(s_perm):
            for i in range(1, len(s_perm) - 1):
                palindrome_candidate = s_perm[:i] + s_perm[i].upper() + s_perm[i + 1:]
                if ' '.join((s[start:end + 1], palindrome_candidate)).replace(' ', '') == s[start:end + 1].upper() + palindrome_candidate.upper():
                    palindromes.add(palindrome_candidate)
    return palindromes