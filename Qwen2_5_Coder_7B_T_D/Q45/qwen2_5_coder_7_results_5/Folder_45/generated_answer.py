def palindromes_between_indices(s):
    s = s[5:10].lower()
    chars = ''.join(filter(str.isalpha, s))
    n = len(chars)
    palindromes = set()
    for i in range(n):
        for j in range(i + 3, n + 1):
            word = chars[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes