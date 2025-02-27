def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    result = set()
    for i in range(len(s) - 12):
        for j in range(i + 13, min(i + 50, len(s)) + 1):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if substring == substring[::-1] and 13 <= len(substring) <= 49:
                result.add(substring)
    return result