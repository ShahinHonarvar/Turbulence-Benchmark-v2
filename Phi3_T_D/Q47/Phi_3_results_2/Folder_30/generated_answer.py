def palindromes_of_specific_lengths(s):
    start, end = (14, min(90, len(s)))
    return {s[i:j].lower() for i in range(start, end) for j in range(i + 55, i + 72) if s[i:j].isalpha() and s[i:j].lower() == s[i:j][::-1]}