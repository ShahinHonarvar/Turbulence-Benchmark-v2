def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(11, 88):
        if s[i].isalpha():
            palindromes = {s[i:j] for j in range(i + 1, min(i + 6, 88)) if s[i:j] == s[i:j][::-1]}
            result.update(palindromes)
    return result