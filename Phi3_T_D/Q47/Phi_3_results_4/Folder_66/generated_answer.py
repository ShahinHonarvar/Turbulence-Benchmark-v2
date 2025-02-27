def palindromes_of_specific_lengths(s):
    start, end = (32, 79)
    return {s[i:j].lower() for i in range(start, end + 1) for j in range(i + 35, min(i + 42, end + 1)) if s[i:j].isalpha() and s[i:j].lower() == s[i:j:-1]}