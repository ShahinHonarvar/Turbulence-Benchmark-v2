def if_contains_anagrams(words):
    filtered_words = [word for word in words if len(word) >= 3]
    sorted_words = [sorted(word.lower()) for word in filtered_words]
    word_counts = {}
    for word in sorted_words:
        word_counts[word] = word_counts.get(word, 0) + 1
    anagram_counts = [count for count in word_counts.values() if count >= 55]
    return len(anagram_counts) >= 55