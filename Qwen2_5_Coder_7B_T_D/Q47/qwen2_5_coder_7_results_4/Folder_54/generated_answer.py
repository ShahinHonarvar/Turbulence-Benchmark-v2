def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    result = set()
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
        substring = s[i:i + 19]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result