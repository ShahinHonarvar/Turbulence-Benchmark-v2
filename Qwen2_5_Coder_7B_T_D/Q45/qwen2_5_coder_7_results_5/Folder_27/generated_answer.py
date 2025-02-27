def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s), 5, -1):
        for perm in permutations(s, i):
            if ''.join(perm).lower() == ''.join(perm)[::-1].lower():
                palindromes.add(''.join(perm))
    return palindromes