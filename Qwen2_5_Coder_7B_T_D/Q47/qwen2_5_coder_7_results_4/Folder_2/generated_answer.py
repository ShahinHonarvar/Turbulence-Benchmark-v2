def palindromes_of_specific_lengths(s):
    s = s[10:60].lower()
    result = set()
    for i in range(len(s) - 17):
        for j in range(18, 37):
            if s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                result.add(s[i:i + j])
    return result