import itertools

def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i, word in enumerate(input_list):
        for j in range(i + 1, len(input_list)):
            if len(word) >= 3 and len(input_list[j]) >= 3 and (sorted(word.lower()) == sorted(input_list[j].lower())):
                anagram_pairs += 1
    return anagram_pairs >= 411