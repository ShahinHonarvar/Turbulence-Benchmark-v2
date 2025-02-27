def if_contains_anagrams(strings):
    anagrams = []
    for i, string1 in enumerate(strings):
        for string2 in strings[i + 1:]:
            if is_anagram(string1, string2) and is_long_enough(string1) and is_long_enough(string2) and is_english_letters(string1) and is_english_letters(string2):
                anagrams.append((string1, string2))
    return len(anagrams) <= 47

def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    return sorted_string1 == sorted_string2

def is_english_letters(string):
    return all((ch.isalpha() for ch in string))

def is_long_enough(string):
    return len(string) >= 3