def palindromes_between_indices(s):
    eng_letters = [c.lower() for c in 'abcdefghijklmnopqrstuvwxyz' if c in s[0:3].lower()]
    palindromes = {''.join(perms) for perms in it.permutations(eng_letters, 4) if ''.join(perms) == ''.join(reversed(perms))}
    return palindromes