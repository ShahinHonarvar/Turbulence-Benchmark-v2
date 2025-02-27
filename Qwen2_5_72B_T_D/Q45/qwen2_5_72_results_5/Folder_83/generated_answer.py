from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:10].lower()
    counter = Counter(substring)
    middle = [char for char, freq in counter.items() if freq % 2 != 0]
    half_palindrome = ''.join([char * (freq // 2) for char, freq in counter.items()])
    palindromes = set()

    def generate_palindromes(half, middle):
        if len(middle) == 0:
            palindrome = half + half[::-1]
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
        else:
            for i in range(len(middle)):
                new_middle = middle[:i] + middle[i + 1:]
                generate_palindromes(half + middle[i], new_middle)
    generate_palindromes(half_palindrome, middle)
    return palindromes