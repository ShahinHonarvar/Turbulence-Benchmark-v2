def palindromes_between_indices(s):
    target_chars = set(s[1:6])
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def gen_permutations(chars):
        if len(chars) == 0:
            yield ''
            return
        first_char = chars[0]
        remaining = chars[1:]
        for perm in gen_permutations(remaining):
            for i in range(len(perm) + 1):
                yield (perm[:i] + first_char + perm[i:])
    for perm in gen_permutations(target_chars):
        if len(perm) >= 6 and is_palindrome(perm):
            palindromes.add(perm.lower())
    return palindromes