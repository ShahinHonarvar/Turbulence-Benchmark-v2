def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(127, 289):
        for j in range(i + 119, min(289, i + 142)):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result