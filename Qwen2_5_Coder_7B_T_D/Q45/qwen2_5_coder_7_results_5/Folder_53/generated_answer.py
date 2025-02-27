def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join([c for c in s if c in letters])
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(sorted(substring)))
    return palindromes