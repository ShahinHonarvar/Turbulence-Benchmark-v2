from collections import Counter

def palindromes_between_indices(s):

    def generate_palindromes(counter, length):

        def generate_half_palindrome(freqs, half_length, current):
            if len(current) == half_length:
                yield current
                return
            for char in freqs:
                if freqs[char] > 0:
                    freqs[char] -= 2
                    yield from generate_half_palindrome(freqs, half_length, current + char)
                    freqs[char] += 2
        half_length = length // 2
        for char in counter:
            if counter[char] % 2 == 1 and length % 2 == 1:
                rest = {k: v // 2 for k, v in counter.items() if k != char}
                for half in generate_half_palindrome(rest, half_length, ''):
                    yield (half + char + half[::-1])
            else:
                rest = {k: v // 2 for k, v in counter.items()}
                for half in generate_half_palindrome(rest, half_length, ''):
                    yield (half + half[::-1])
    substring = s[1:7].lower()
    counter = Counter(substring)
    valid_palindromes = {palindrome for palindrome in generate_palindromes(counter, 6) if len(palindrome) == 6}
    return valid_palindromes