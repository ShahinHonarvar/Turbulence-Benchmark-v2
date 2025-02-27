def palindromes_of_specific_lengths(text):
    result_set = set()
    text = text[25:85].lower()
    for length in range(30, 47):
        for i in range(26, 85 - length + 1):
            substring = text[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result_set.add(substring)
    return result_set