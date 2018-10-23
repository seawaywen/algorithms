#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time

def timeit(is_log_on=False):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            exe_time = time.time() - start_time

            if is_log_on:
                print(result)

            print(f'func[{func.__name__}] exe time:{exe_time}')
            return result
        return _wrapper
    return wrapper


