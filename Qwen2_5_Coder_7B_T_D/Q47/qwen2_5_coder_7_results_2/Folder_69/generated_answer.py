def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for start in range(11, 97):
        for length in range(45, 53):
            end = start + length
            if end <= 97 and s[start:end] == s[start:end][::-1] and s[start:end].isalpha():
                result.add(s[start:end])
    return result