def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(1, 300):
        for j in range(i + 2, min(301, i + 11)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result