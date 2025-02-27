def palindromes_between_indices(s):
    substring = s[5:8].lower()
    unique_chars = set(substring)
    palindrome_set = set()

    def generate_palindromes(chars, length):
        if length == 3:
            for i in range(len(chars)):
                for j in range(len(chars)):
                    palindrome = chars[i] + chars[j] + chars[i]
                    yield palindrome
        else:
            for char in chars:
                yield from generate_palindromes(chars, length - 2)
    for length in range(3, 4):
        for palindrome in generate_palindromes(list(unique_chars), length):
            palindrome_set.add(palindrome)
    return palindrome_set