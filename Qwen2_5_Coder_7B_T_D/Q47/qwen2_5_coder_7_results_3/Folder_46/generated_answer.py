def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 98):
        for j in range(i + 2, 98):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and 29 <= len(substring) <= 62 and substring.isalpha():
                result.add(substring)
    return result