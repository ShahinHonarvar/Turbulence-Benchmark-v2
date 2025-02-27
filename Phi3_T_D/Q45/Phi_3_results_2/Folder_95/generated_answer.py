def palindromes_between_indices(s):
    substring = s[6:10]
    substring = substring.lower()
    letters = ''.join(sorted(set(substring)))
    palindromes = set()

    def backtrack(path='', index=0):
        if len(path) >= 3 and path == path[::-1]:
            palindromes.add(path)
        for i in range(index, len(letters)):
            backtrack(path + letters[i], i)
    backtrack()
    return palindromes