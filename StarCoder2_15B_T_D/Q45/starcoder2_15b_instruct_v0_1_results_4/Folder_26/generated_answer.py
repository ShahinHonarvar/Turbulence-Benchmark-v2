def palindromes_between_indices(string):
    s = string[4:7].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s)):
            palindromes.add(s[i:j + 1])
    return palindromes