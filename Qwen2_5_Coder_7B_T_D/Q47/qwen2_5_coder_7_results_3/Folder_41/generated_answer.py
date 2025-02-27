def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:8].lower()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 5, len(s) + 1)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result