def palindromes_of_specific_lengths(s):
    substr = s[18:88].lower()
    result = set()
    for i in range(len(substr)):
        for j in range(i + 38, min(i + 61, len(substr) + 1)):
            substring = substr[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result