def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(31, 75):
        for j in range(i + 23, min(75, i + 40)):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result