from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    counter = Counter(substring)
    available_chars = ''.join([char * freq for char, freq in counter.items()])
    result_set = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4:
            result_set.add(current)
        if len(remaining) < 2:
            return
        for i in range(len(remaining)):
            if i == 0 or remaining[i] != remaining[i - 1]:
                generate_palindromes(remaining[i] + current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', available_chars)
    return result_set