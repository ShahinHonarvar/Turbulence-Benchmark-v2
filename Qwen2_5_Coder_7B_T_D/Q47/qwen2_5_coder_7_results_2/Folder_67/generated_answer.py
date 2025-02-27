def palindromes_of_specific_lengths(s):
    result = set()
    s = s[65:100]
    s = s.lower()
    for i in range(len(s) - 25):
        substring = s[i:i + 34]
        if substring == substring[::-1] and substring.isalpha() and (26 <= len(substring) <= 33):
            result.add(substring)
    return result