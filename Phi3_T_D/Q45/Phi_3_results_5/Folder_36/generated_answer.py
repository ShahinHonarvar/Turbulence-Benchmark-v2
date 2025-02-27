import itertools

def palindromes_between_indices(s):
    middle_chunk = s[5:9].lower()
    english_letters = ''.join(set(middle_chunk) & set('abcdefghijklmnopqrstuvwxyz'))
    palindromes = set()
    for i in range(len(english_letters), 0, -1):
        if len(english_letters) % i == 0:
            possible_combinations = len(english_letters) // i
            for combination in itertools.combinations_with_replacement(english_letters, i):
                if ''.join(combination) == ''.join(reversed(combination)):
                    palindrome = ''.join(combination) * possible_combinations
                    if len(palindrome) >= 3:
                        palindromes.add(palindrome)
    return palindromes