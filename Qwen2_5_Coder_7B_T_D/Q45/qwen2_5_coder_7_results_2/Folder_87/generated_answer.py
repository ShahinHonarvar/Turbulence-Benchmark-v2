def palindromes_between_indices(s):
    s = s[3:10]
    s = s.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub in letters and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes