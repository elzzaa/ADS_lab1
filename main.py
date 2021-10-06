import random
import sorts
import matplotlib.pyplot as plt


def generate_list(lst_type: str, size: int):
    if lst_type == "random":
        return [random.randint(0, 1000) for _ in range(size)]
    elif lst_type == "sorted_increase":
        return [i for i in range(size)]
    elif lst_type == "sorted_decrease":
        return [i for i in range(size)][::-1]
    elif lst_type == "repeated":
        return [random.randint(1, 3) for _ in range(size)]


def experiment(exp_type: str):
    selection_var, insertion_var, merge_var, shell_var = [[], []], [[], []], [[], []], [[], []]
    selection_sum, insertion_sum, merge_sum, shell_sum = [0, 0], [0, 0], [0, 0], [0, 0]
    selection_time, insertion_time, merge_time, shell_time = [], [], [], []
    selection_comp, insertion_comp, merge_comp, shell_comp = [], [], [], []

    for size in [2 ** i for i in range(7, 15)]:
        for _ in range(5):
            random_list = generate_list(exp_type, size)

            selection_sorted = sorts.selection(random_list)
            selection_var[0].append(selection_sorted["working_time"])
            selection_var[1].append(selection_sorted["comparison_num"])

            insertion_sorted = sorts.insertion(random_list)
            insertion_var[0].append(insertion_sorted["working_time"])
            insertion_var[1].append(insertion_sorted["comparison_num"])

            merge_sorted = sorts.merge(random_list)
            merge_var[0].append(merge_sorted["working_time"])
            merge_var[1].append(merge_sorted["comparison_num"])

            shell_sorted = sorts.shell(random_list)
            shell_var[0].append(shell_sorted["working_time"])
            shell_var[1].append(shell_sorted["comparison_num"])

        for i in range(2):
            for j in range(5):
                selection_sum[i] += selection_var[i][j]
                insertion_sum[i] += insertion_var[i][j]
                merge_sum[i] += merge_var[i][j]
                shell_sum[i] += shell_var[i][j]

        selection_time.append(selection_sum[0] / 5)
        selection_comp.append(selection_sum[1] / 5)
        insertion_time.append(insertion_sum[0] / 5)
        insertion_comp.append(insertion_sum[1] / 5)
        merge_time.append(merge_sum[0] / 5)
        merge_comp.append(merge_sum[1] / 5)
        shell_time.append(shell_sum[0] / 5)
        shell_comp.append(shell_sum[1] / 5)

    return {"time": [selection_time, insertion_time, merge_time, shell_time],
            "comparisons": [selection_comp, insertion_comp, merge_comp, shell_comp]}


def plot_drawing(exp_res, name):
    # plot for sorting time
    plt.ylabel("sorting time")
    plt.xlabel("array size")
    plt.plot([i for i in range(7, 15)], exp_res["time"][0], label="selection sort")
    plt.plot([i for i in range(7, 15)], exp_res["time"][1], label="insertion sort")
    plt.plot([i for i in range(7, 15)], exp_res["time"][2], label="merge sort")
    plt.plot([i for i in range(7, 15)], exp_res["time"][3], label="shell sort")
    plt.yscale("log")
    plt.title(name)
    plt.legend()
    plt.show()

    # plot for number of comparisons
    plt.ylabel("number of comparisons")
    plt.xlabel("array size")
    plt.plot([i for i in range(7, 15)], exp_res["comparisons"][0], label="selection sort")
    plt.plot([i for i in range(7, 15)], exp_res["comparisons"][1], label="insertion sort")
    plt.plot([i for i in range(7, 15)], exp_res["comparisons"][2], label="merge sort")
    plt.plot([i for i in range(7, 15)], exp_res["comparisons"][3], label="shell sort")
    plt.yscale("log")
    plt.legend()
    plt.show()


def random_test():
    """Experiment on random list"""
    exp_res = experiment("random")
    plot_drawing(exp_res, name="Experiment on random list")


def sorted_test():
    """Experiment for sorted in increasing way list."""
    exp_res = experiment("sorted_increase")
    plot_drawing(exp_res, name="Experiment for sorted in increasing way list")


def reverse_test():
    """Experiment for sorted in decreasing way list."""
    exp_res = experiment("sorted_decrease")
    plot_drawing(exp_res, name="Experiment for sorted in decreasing way list")


def repeated_test():
    """Experiment for list with repeated elements from {1, 2, 3}."""
    exp_res = experiment("repeated")
    plot_drawing(exp_res, name="Experiment for list with repeated elements from {1, 2, 3}")


if __name__ == "__main__":
    random_test()
    sorted_test()
    reverse_test()
    repeated_test()
