def palindromes_of_specific_lengths(s):
    s = s[12:123]
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 12, min(i + 221, len(s) + 1)) if s[i:j].isalpha() and s[i:j].lower() == s[i:j][::-1]}
    return palindromes