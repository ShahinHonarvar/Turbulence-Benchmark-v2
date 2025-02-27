from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    counter = Counter(substring)
    middle = [char for char, freq in counter.items() if freq % 2 != 0]
    half_palindrome = ''.join([char * (freq // 2) for char, freq in counter.items()])
    palindromes = set()

    def generate_palindromes(half, middle):
        if len(half) * 2 + len(middle) >= 6:
            if middle:
                palindromes.add(half + ''.join(middle) + half[::-1])
            else:
                palindromes.add(half + half[::-1])

    def backtrack(path, options):
        if len(path) == len(half_palindrome):
            for m in middle:
                generate_palindromes(path, [m])
            if not middle:
                generate_palindromes(path, [])
            return
        for i in range(len(options)):
            if i > 0 and options[i] == options[i - 1]:
                continue
            backtrack(path + options[i], options[:i] + options[i + 1:])
    unique_half = ''.join(sorted(half_palindrome))
    backtrack('', unique_half)
    return palindromes