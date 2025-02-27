def palindromes_of_specific_lengths(s):
    s = s[10:75].lower()
    result = set()
    for i in range(len(s) - 5):
        for j in range(6, 9):
            if s[i:i + j] == s[i:i + j][::-1]:
                result.add(s[i:i + j])
    return result