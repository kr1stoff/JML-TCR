import os
import math
import logging


def get_threads_dict() -> dict:
    """
    获取最大线程数, 高线程分配为 max * 2 / 3, 低线程为 high / 2

    :return dict_thr:   high_threads, low_threads 高/低线程分配数
    """
    logging.info('获取线程数字典')
    max_threads = os.cpu_count()
    high_threads = math.ceil(max_threads * 2 / 3)
    low_threads = math.floor(high_threads / 2)
    dict_thr = {'high': high_threads, 'low': low_threads}

    return dict_thr
