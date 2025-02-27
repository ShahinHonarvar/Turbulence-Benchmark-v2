from collections import Counter

def if_contains_anagrams(string_list):
    length_anagrams = {}
    count = 0
    for word in string_list:
        word_lower = word.lower()
        word_sorted = ''.join(sorted(word_lower))
        word_length = len(word_lower)
        if word_length < 3:
            continue
        if word_sorted in length_anagrams:
            for indexed_anagram in length_anagrams[word_sorted]:
                if indexed_anagram != len(word_lower):
                    length_anagrams[word_sorted].append(len(word_lower))
                    count += 1
                    break
        else:
            length_anagrams[word_sorted] = [len(word_lower)]
    return count <= 24