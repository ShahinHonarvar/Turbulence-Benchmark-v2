from collections import Counter

def palindromes_between_indices(s):
    substring = s[8:10].lower()
    counter = Counter(substring)
    palindromes = set()
    for length in range(3, 11):
        for candidate in generate_palindromes(counter, length):
            palindromes.add(candidate)
    return palindromes

def generate_palindromes(counter, length):
    if length % 2 == 0:
        half_length = length // 2
        for half in generate_half_palindrome(counter, half_length):
            yield (half + half[::-1])
    else:
        half_length = length // 2
        for half in generate_half_palindrome(counter, half_length):
            for char in counter:
                if counter[char] % 2 == 1:
                    yield (half + char + half[::-1])

def generate_half_palindrome(counter, half_length):
    if half_length == 0:
        yield ''
    else:
        for char in counter:
            if counter[char] > 1:
                counter[char] -= 2
                for half in generate_half_palindrome(counter, half_length - 1):
                    yield (char + half)
                counter[char] += 2