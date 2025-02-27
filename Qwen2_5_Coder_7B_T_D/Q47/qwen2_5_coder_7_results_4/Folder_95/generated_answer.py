def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    result = set()
    for i in range(len(s) - 19):
        substring = s[i:i + 21]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result