def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    n = 62
    for i in range(len(text) - n + 1):
        for j in range(i + n - 1, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                result.add(text[i:j + 1])
    return result