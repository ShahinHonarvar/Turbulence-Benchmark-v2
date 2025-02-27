def palindromes_of_specific_lengths(s):
    start, end = (15, 73)
    palindromes = {s[i:j] for i in range(start, end) for j in range(i + 19, end + 1) if s[i:j].isalpha() and s[i:j].lower() == s[i:j].lower()[::-1]}
    return {p for p in palindromes if 19 <= len(p) <= 55}