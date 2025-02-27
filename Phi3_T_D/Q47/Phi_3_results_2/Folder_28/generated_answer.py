def palindromes_of_specific_lengths(s):
    s = s[31:72].lower()
    palindromes = {s[i:j] for i in range(20, 32) for j in range(i + 20, 33) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}
    return palindromes