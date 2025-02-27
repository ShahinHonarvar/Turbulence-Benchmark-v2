def palindromes_of_specific_lengths(s):
    s = s[18:88]
    palindromes = {s[i:i + l] for l in range(38, 61) for i in range(len(s) - l + 1) if s[i:i + l].isalpha() and s[i:i + l].lower() == s[i:i + l][::-1].lower()}
    return palindromes