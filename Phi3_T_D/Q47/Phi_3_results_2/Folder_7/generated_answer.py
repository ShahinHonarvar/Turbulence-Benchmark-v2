def palindromes_of_specific_lengths(s):
    s = s[118:256].lower()
    return {s[i:i + l] for l in range(104, 124) for i in range(len(s) - l + 1) if s[i:i + l].isalpha() and s[i:i + l] == s[i:i + l][::-1]}