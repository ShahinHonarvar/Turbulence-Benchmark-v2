def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 474 + 1):
        substring = text[i:i + 474]
        if substring == substring[::-1]:
            if substring.isalpha():
                result.add(substring)
    return result