def palindromes_between_indices(s):
    sub_str = s[4:10].lower()
    letters = ''.join(sub_str.split())
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes