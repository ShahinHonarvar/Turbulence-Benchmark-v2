def palindromes_between_indices(s):
    s = s[1:3].lower()
    letters = set(s)
    palindromes = set()
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = sorted(s[i:i + length])
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes