from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:6]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def gen_permutations(chars):
        for i in range(3, len(chars) + 1):
            for perm in permutations(chars, i):
                if is_palindrome(''.join(perm).lower()):
                    palindromes.add(''.join(perm).lower())
    gen_permutations(sub_str)
    return palindromes