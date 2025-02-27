def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 6):
        for j in range(i + 3, min(i + 7, len(s))):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result