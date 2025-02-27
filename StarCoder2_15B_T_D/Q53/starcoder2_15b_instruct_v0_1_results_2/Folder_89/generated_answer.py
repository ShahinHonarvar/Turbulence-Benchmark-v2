def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 43, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result