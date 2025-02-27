def palindromes_of_specific_lengths(s):
    s = s[10:75].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 6, min(i + 9, len(s) + 1)) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}
    return set(palindromes)