def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 2):
        if i <= 4:
            for j in range(i + 2, min(i + 5, len(s) + 1)):
                substring = s[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result