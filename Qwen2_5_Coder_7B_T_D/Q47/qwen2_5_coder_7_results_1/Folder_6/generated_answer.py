def palindromes_of_specific_lengths(s):
    result = set()
    s = s[45:99].lower()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if substring == substring[::-1]:
            result.add(substring)
    return result