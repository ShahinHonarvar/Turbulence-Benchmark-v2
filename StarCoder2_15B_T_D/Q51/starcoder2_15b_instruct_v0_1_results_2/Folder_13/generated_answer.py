import collections

def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i, word1 in enumerate(input_list):
        for j, word2 in enumerate(input_list):
            if i != j and len(word1) >= 3 and (len(word2) >= 3):
                word1_counter = collections.Counter(word1.lower())
                word2_counter = collections.Counter(word2.lower())
                if word1_counter == word2_counter:
                    anagram_pairs += 1
                    if anagram_pairs > 54:
                        return False
    return anagram_pairs <= 54