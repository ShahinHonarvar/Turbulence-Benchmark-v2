def palindromes_of_specific_lengths(s):
    s = s[10:71]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 53, len(s) + 1)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result