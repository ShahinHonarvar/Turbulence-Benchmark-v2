def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    result = set()
    for i in range(n):
        for j in range(i + 6, n + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result