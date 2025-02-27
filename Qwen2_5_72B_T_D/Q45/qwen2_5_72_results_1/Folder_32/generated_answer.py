from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:8]
    counter = Counter(filter(str.isalpha, substring.lower()))
    odds = sum((1 for count in counter.values() if count % 2 != 0))
    palindromes = set()
    if odds <= 1:

        def generate_palindromes(counter, length, prefix=''):
            if len(prefix) == (length - odds) // 2:
                for char in counter:
                    if counter[char] % 2 != 0:
                        palindromes.add(prefix + char + prefix[::-1])
                if odds == 0:
                    palindromes.add(prefix + prefix[::-1])
            else:
                for char in counter:
                    if counter[char] > 1:
                        counter[char] -= 2
                        generate_palindromes(counter, length, prefix + char)
                        counter[char] += 2
        for length in range(5, 8):
            if sum((count // 2 for count in counter.values())) >= (length - odds) // 2:
                generate_palindromes(counter, length)
    return palindromes