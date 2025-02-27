def if_contains_anagrams(str_list):
    anagram_count = 0
    sorted_anagrams = {}
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in sorted_anagrams:
                sorted_anagrams[sorted_word].append(word)
                anagram_count += len(sorted_anagrams[sorted_word]) - 1
            else:
                sorted_anagrams[sorted_word] = [word]
    return anagram_count >= 178