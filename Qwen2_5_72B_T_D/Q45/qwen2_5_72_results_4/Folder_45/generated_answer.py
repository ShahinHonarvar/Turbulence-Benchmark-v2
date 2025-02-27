from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letter_counts = Counter(substring)
    even_letters = [letter for letter, count in letter_counts.items() if count % 2 == 0]
    odd_letters = [letter for letter, count in letter_counts.items() if count % 2 != 0]
    if len(even_letters) + (len(odd_letters) > 0) < 2:
        return set()
    half_palindromes = ['']
    for letter in even_letters:
        new_half_palindromes = []
        for half in half_palindromes:
            new_half_palindromes.append(half + letter)
        half_palindromes.extend(new_half_palindromes)
    palindromes = set()
    for half in half_palindromes:
        if len(half) * 2 >= 4:
            palindromes.add(half + half[::-1])
        if len(odd_letters) > 0:
            for odd in odd_letters:
                if len(half) * 2 + 1 >= 4:
                    palindromes.add(half + odd + half[::-1])
    return palindromes