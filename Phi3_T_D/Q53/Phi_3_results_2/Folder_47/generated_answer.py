def palindrome_of_length_at_least_n(text):
    text = text.lower()
    longest_palindrome = set()
    for i in range(len(text)):
        for j in range(i + 77, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                longest_palindrome.add(substring)
    return longest_palindrome