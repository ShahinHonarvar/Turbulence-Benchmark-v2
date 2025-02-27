def palindromes_between_indices(s):
    subset = {char.lower() for char in s[:6]}
    if len(subset) < 3:
        return set()

    def is_palindrome(s):
        return s == s[::-1]

    def find_palindromes(length, current, used):
        if length == 0:
            if len(current) >= 3 and is_palindrome(current):
                yield current
            return
        for char in subset - used:
            new_used = used | {char}
            yield from find_palindromes(length - 1, current + char, new_used)
    result = set()
    for i in range(3, len(subset) + 1):
        yield from find_palindromes(i, '', set())
    return result