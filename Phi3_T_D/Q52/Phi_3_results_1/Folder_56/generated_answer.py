def palindrome_of_length_n(string):
    result = set()
    str_lower = string.lower()
    for i in range(len(str_lower) - 86):
        substr = str_lower[i:i + 95]
        if substr.isalpha() and substr == substr[::-1]:
            result.add(substr)
    return result