def palindromes_of_specific_lengths(text):
    result = set()
    for start in range(101):
        for end in range(start + 3, min(101, start + 16)):
            substring = text[start:end].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result