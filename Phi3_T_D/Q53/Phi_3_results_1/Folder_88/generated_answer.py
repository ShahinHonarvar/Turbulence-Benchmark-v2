from re import findall
    from itertools import combinations

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    combinations_of_27_letters = [''.join(letters) for letters in combinations(english_letters, 27)]
    all_palindromes = set()
    for combination in combinations_of_27_letters:
        positions = [m.start() for m in findall(f'(?=({combination}))', s)]
        for position in positions:
            length = len(combination)
            max_poss_position = len(s) - length
            if position > max_poss_position:
                continue
            candidate = s[position:position + length]
            if candidate.upper() == candidate[::-1]:
                all_palindromes.add(candidate.lower())
    return all_palindromes