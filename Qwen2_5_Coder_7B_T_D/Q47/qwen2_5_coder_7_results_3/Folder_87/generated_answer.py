def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 94):
        for j in range(i + 33, min(94, i + 55)):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result