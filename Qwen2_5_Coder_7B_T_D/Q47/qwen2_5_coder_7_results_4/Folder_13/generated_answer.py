def palindromes_of_specific_lengths(s):
    result = set()
    s = s[13:96].lower()
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result