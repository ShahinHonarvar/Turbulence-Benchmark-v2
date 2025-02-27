def palindrome_of_length_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text) - 5):
        substr = text[i:i + 6]
        if substr == substr[::-1]:
            result.add(substr)
    return result