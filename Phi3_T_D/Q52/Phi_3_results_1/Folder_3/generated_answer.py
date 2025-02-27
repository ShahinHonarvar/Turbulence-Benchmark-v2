def palindrome_of_length_n(s):
    length = 50
    lower_s = s.lower()
    palindromes = {lower_s[i:j + 1] for i in range(len(lower_s) - length + 1) for j in range(i + length - 1, len(lower_s)) if lower_s[i:j + 1] == lower_s[i:j + 1][::-1]}
    return {p.upper() for p in palindromes}