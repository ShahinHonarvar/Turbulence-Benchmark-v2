def palindromes_of_specific_lengths(s):
    s = s[24:98].lower()
    result = set()
    for start in range(len(s)):
        for length in range(10, 37):
            end = start + length
            if end <= len(s) and s[start:end] == s[start:end][::-1] and s[start:end].isalpha():
                result.add(s[start:end])
    return result