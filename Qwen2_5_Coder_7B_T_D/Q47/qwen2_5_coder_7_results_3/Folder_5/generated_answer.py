def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 4, min(len(s), i + 6)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result