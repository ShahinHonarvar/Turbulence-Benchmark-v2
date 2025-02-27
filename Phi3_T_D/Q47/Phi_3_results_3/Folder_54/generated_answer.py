def palindromes_of_specific_lengths(s):
    start, end = (27, 77)
    s = s[start:end + 1]
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 18, i + 19 + 1) if s[i:j].isalpha() and s[i:j].lower() == s[i:j][::-1]}
    return palindromes