def palindromes_of_specific_lengths(s):
    s = s[24:98]
    palindromes = {s[i:j] for i in range(98 - 24) for j in range(i + 10, min(i + 37, 98 - i)) if s[i:j].isalpha() and s[i:j].lower() == s[i:j][::-1]}
    return palindromes