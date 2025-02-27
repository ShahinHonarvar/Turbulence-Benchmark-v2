def palindromes_of_specific_lengths(s):
    seq = s[12:93]
    result = set()
    for length in range(17, 67):
        for i in range(len(seq) - length + 1):
            substr = seq[i:i + length].lower()
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result