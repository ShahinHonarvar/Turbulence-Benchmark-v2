from Q12.qwen2_5_coder_32_results_3.Folder_56.generated_answer import find_smallest_num
import random


def test_result_is_in_range():
    initial_list = [i for i in range(0,(8 + 1) * 1000)]
    result = find_smallest_num(initial_list)
    assert result in initial_list[1:8+1]


def test_large_range():
    large_list = [i for i in range(0,(8 + 1) * 1000)]
    expected_result = large_list[1]
    assert find_smallest_num(large_list) == expected_result


def test_all_zero_range():
    zero_list = [0 for _ in range(0,(8 + 1) * 5)]
    assert find_smallest_num(zero_list) == 0


def test_all_n_range():
    for n in range(-10,11):
        initial_list = [n for _ in range(0, 8 + 10)]
        assert find_smallest_num(initial_list) == n


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, (8 + 1) * 3)]
    random.shuffle(initial_list)
    sliced_list = initial_list[1:8 + 1]
    sliced_list.sort()
    assert find_smallest_num(initial_list) == min(sliced_list)


def test_reversed_range():
    initial_list = [i for i in range(-1000, (8 + 1) * 3)]
    initial_list.reverse()
    expected_result = initial_list[8]
    assert find_smallest_num(initial_list) == expected_result


def test_result_is_the_smallest_in_range():
    initial_list = [i for i in range(-1000, (8 + 1) * 3)]
    random.shuffle(initial_list)
    sliced_list = initial_list[1:8 + 1]
    result = find_smallest_num(initial_list)
    for i in sliced_list:
        assert result <= i