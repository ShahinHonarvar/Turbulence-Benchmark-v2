from Q26.qwen2_5_coder_7_results_3.Folder_33.generated_answer import sum_in_range
import random


def test_range_of_given_arguments():
    initial_list = list(range(368, 679 + 1))
    assert sum_in_range(initial_list) == sum(initial_list)


def test_zeros():
    zero_list = [0 for _ in range(368 - 100, 679 + 100)]
    assert sum_in_range(zero_list) == 0


def test_nums():
    for n in range(368,679+1):
        num_list = [n for _ in range(368 - 100, 679 + 100)]
        assert sum_in_range(num_list) == sum(num_list)


def test_compare_sums():
    initial_list = [i for i in range(0, 1000)]
    assert sum_in_range(initial_list) <= sum(initial_list)


def test_out_of_given_arguments_range():
    l = []
    while len(l) < 20:
        random_int = random.randint(368 - 100, 368 - 1)
        l.append(random_int)
    assert sum_in_range(l) == 0