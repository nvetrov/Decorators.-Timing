import time


"""Подсказка
Для использования того же класса в качестве контекстного менеджера, 
мы должны добавить __enter__ и __exit__, но при этом число прогонов остаётся на "совести" использующего класс человека: 
дополнительные циклы придётся добавлять внутри блока with. """
NUM_RUNS = 1000


class Timing:
    def __init__(self, function_to_run, num_runs=100):
        self.num_runs = num_runs
        self.func_to_run = function_to_run
        self.start = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args, **kwargs):
        avg_time = (time.time() - self.start) / self.num_runs
        print("Среднее время выполнения, мкс = %.5f" % (avg_time * 1_000_000))


def res(param=1000):  # функция для проверки работы декоратора
    for i in range(1, param):
        a = i ** 2
        # print(a)


with Timing(res, NUM_RUNS) as ts:
    for i in range(NUM_RUNS):
        res()
