def palindromes_of_specific_lengths(s):
    s = s[62:89]
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 18, min(i + 22, len(s) + 1)) if s[i:j].isalpha() and s[i:j].lower() == s[i:j][::-1].lower()}
    return palindromes