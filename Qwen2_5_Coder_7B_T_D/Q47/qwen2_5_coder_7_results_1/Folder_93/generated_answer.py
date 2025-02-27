def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[17:96].lower()
    for i in range(len(substr)):
        for j in range(i + 13, min(i + 50, len(substr) + 1)):
            substring = substr[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result