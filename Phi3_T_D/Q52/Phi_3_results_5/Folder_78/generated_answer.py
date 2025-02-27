def palindrome_of_length_n(s):
    S = s.lower()
    palindromes = set()
    n = len(S)
    for i in range(n - 47):
        substring = S[i:i + 48]
        if substring == substring[::-1]:
            palindromes.add(substring.upper())
    return palindromes