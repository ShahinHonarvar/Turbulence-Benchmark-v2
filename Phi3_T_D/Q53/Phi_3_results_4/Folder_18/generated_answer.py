def palindrome_of_length_at_least_n(s):
    candidates = {s[i:i + n] for n in range(57, len(s) + 1) for i in range(len(s) - n + 1)}
    return {item for item in candidates if item.lower() == item.lower()[::-1] and item.isalpha()}