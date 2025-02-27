def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    n = 5
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result