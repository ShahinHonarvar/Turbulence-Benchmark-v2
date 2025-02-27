def if_contains_anagrams(words):
    min_length = 3
    word_dict = {}
    anagram_count = 0
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= min_length:
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word.lower())
                anagram_count += 1
            else:
                word_dict[sorted_word] = [word.lower()]
    pairs = [v for v in word_dict.values() if len(v) > 1]
    total_pairs = sum((len(group) // 2 for group in pairs))
    return total_pairs >= 189