def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(11, 98):
        for j in range(i + 29, min(len(s) - i, 63) + i):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result