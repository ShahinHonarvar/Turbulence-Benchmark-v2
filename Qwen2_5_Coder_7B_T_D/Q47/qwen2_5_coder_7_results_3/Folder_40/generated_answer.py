def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:6].lower()
    for i in range(3, 6):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result