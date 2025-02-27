def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[11:84]
    for length in range(37, 61):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                result.add(substr)
    return result