from collections import Counter

def palindromes_between_indices(s):

    def generate_palindromes(letters, min_length):

        def generate(half, count):
            if len(half) * 2 + (len(half) & 1) >= min_length:
                palindromes.add(half + half[::-1][len(half) & 1:])
            if count < len(letters):
                for i in range(count + 1):
                    generate(half + letters[count] * i, count + 1)
        palindromes = set()
        generate('', 0)
        return palindromes
    substring = s[1:9].lower()
    letter_counts = Counter(filter(str.isalpha, substring))
    letters = ''.join([char * (count // 2) for char, count in letter_counts.items()])
    if len(letters) < 3:
        return set()
    return generate_palindromes(letters, 0)