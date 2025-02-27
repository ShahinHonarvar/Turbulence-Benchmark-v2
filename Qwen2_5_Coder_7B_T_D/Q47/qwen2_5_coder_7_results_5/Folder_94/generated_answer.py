def palindromes_of_specific_lengths(s):
    result = set()
    s = s[40:95].lower()
    for start in range(len(s) - 51 + 1):
        for length in range(45, 52):
            if s[start:start + length] == s[start:start + length][::-1] and s[start:start + length].isalpha():
                result.add(s[start:start + length])
    return result