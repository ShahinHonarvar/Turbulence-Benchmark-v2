import string

def palindromes_of_specific_lengths(s):
    s = s[124:284].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 115, min(i + 135, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and all((c in string.ascii_lowercase for c in s[i:j])):
                result.add(s[i:j])
    return result