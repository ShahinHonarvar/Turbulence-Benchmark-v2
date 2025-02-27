def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    result = set()
    for i in range(n):
        for j in range(i + 13, n + 1):
            candidate = text[i:j]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result