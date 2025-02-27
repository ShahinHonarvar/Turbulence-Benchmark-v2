def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(2, 9):
        for j in range(i, i + 5):
            substring = s[i:j]
            if len(substring) >= 3 and len(substring) <= 4 and substring.isalpha():
                if substring.lower() == substring[::-1].lower():
                    result.add(substring)
    return result