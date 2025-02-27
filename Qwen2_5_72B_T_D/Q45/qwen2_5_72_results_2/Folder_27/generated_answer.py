from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    counter = Counter(substring)
    available_chars = ''.join([char * freq for char, freq in counter.items() if char.isalpha()])

    def generate_palindromes(available_chars, min_length):

        def backtrack(path):
            if len(path) > 2:
                if path == path[::-1]:
                    if len(path) >= min_length:
                        palindromes.add(path)
            for i in range(len(available_chars)):
                if counts[i] > 0:
                    counts[i] -= 1
                    backtrack(path + available_chars[i])
                    counts[i] += 1
        palindromes = set()
        counts = [available_chars.count(char) for char in set(available_chars)]
        backtrack('')
        return palindromes
    return generate_palindromes(available_chars, 6)