def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(6, 10):
        for start in range(29, 99):
            end = start + length
            if end <= 99 and s[start:end] == s[start:end][::-1] and s[start:end].isalpha():
                result.add(s[start:end])
    return result