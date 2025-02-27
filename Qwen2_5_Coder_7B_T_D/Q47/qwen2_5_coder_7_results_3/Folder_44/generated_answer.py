def palindromes_of_specific_lengths(s):
    result = set()
    s = s[18:99].lower()
    for i in range(31, 52):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result