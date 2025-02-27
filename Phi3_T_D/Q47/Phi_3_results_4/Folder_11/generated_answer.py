def palindromes_of_specific_lengths(s):
    substring = s[24:98]
    result = set()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                result.add(substr)
    return result