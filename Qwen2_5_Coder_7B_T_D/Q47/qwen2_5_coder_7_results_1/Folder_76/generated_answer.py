def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(101, 293):
        for j in range(i + 154, min(i + 183, len(s) + 1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result