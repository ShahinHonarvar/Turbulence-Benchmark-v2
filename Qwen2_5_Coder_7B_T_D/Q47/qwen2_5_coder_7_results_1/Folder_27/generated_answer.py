def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    result = set()
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if substring == substring[::-1]:
            result.add(substring)
    return result