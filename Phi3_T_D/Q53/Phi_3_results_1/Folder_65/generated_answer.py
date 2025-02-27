def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 15, len(text) + 1):
            candidate = text[i:j]
            if candidate == candidate[::-1]:
                result.add(candidate.upper())
    return result