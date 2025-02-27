def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    result = set()
    for start in range(len(s) - 49):
        for end in range(start + 49, min(start + 60, len(s))):
            substring = s[start:end + 1]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result