import time


def selection(lst: list):
    """Implementation of selection sort."""
    comparison_num = 0
    working_time = time.time()
    n = len(lst)
    for i in range(n):
        small = i
        for j in range(i + 1, n):
            if lst[small] > lst[j]:
                small = j
            comparison_num += 1
        lst[i], lst[small] = lst[small], lst[i]
    working_time = time.time() - working_time
    return {"sorted_lst": lst, "working_time": working_time, "comparison_num": comparison_num}


def insertion(lst: list):
    """Implementation of insertion sort."""
    comparison_num = 0
    working_time = time.time()
    for i in range(1, len(lst)):
        comparison_num += 1
        current = lst[i]
        pos = i
        while pos > 0 and lst[pos - 1] > current:
            comparison_num += 2
            lst[pos] = lst[pos - 1]
            pos = pos - 1
        lst[pos] = current
    working_time = time.time() - working_time
    # comparison_num = (len(a)**2 - len(a))/4
    return {"sorted_lst": lst, "working_time": working_time, "comparison_num": comparison_num}


def merge(lst: list):
    """Implementation of merge sort"""
    comparison_num = 0
    working_time = time.time()
    if len(lst) > 1:
        r = len(lst) // 2
        l = lst[:r]
        m = lst[r:]
        merge(l)
        merge(m)
        i = j = k = 0
        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                lst[k] = l[i]
                i += 1
            else:
                lst[k] = m[j]
                j += 1
            k += 1
            comparison_num += 1
        while i < len(l):
            lst[k] = l[i]
            i += 1
            k += 1
        while j < len(m):
            lst[k] = m[j]
            j += 1
            k += 1
    working_time = time.time() - working_time
    return {"sorted_lst": lst, "working_time": working_time, "comparison_num": comparison_num}


def shell(lst: list):
    comparison_num = 0
    working_time = time.time()
    i = int(len(lst) / 2)
    while i > 0:
        for j in range(i, len(lst)):
            k = j - i
            while k >= 0:
                if lst[k + i] >= lst[k]:
                    comparison_num += 1
                    break
                else:
                    comparison_num += 1
                    tmp = lst[k]
                    lst[k] = lst[k + i]
                    lst[k + i] = tmp
                k -= i
        i = int(i / 2)
    working_time = time.time() - working_time
    return {"sorted_lst": lst, "working_time": working_time, "comparison_num": comparison_num}
