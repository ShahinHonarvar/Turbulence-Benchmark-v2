def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string) - 84 + 1):
        for j in range(i + 84, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and all((ch.isalpha() for ch in substring)):
                result.add(substring)
    return result