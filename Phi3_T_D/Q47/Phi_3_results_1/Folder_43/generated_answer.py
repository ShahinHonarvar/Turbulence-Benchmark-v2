def palindromes_of_specific_lengths(string):
    result_set = set()
    substring = string[41:90]
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                result_set.add(substr)
    return result_set