def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    result = set()
    for i in range(len(s) - 49):
        for j in range(i + 50, min(i + 54, len(s)) + 1):
            substr = ''.join(filter(str.isalpha, s[i:j]))
            if len(substr) in range(50, 54) and substr == substr[::-1]:
                result.add(substr)
    return result