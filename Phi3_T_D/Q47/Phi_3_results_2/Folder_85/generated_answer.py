def palindromes_of_specific_lengths(s):
    start, end = (29, 98)
    extracted = s[start:end + 1].lower()
    result = set()
    for length in range(6, 10):
        for i in range(end - length + 1):
            substring = extracted[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result