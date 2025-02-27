def palindromes_between_indices(s):
    letters = s[3:9]
    letters = letters.lower()
    letters = ''.join(filter(str.isalpha, letters))
    result = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substr = letters[i:j + 1]
            if len(substr) >= 5 and substr == substr[::-1]:
                result.add(substr)
    return result