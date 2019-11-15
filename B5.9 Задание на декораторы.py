import time

"""
в данном случае внутри вложенной функции (где-то в декораторе) стоит выводить среднее время выполнения;
можно либо зафиксировать число запусков, либо передавать как параметр.
Опционально: вы можете выполнить несколько дополнительных требований и получить за них баллы:

задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера;
задание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера, который можно использовать как контекстный менеджер.
"""


# TODO: Кстати, вот наблюдение. В юните B5.7 была задачка на последовательность Фибоначчи. Если увеличить верхнюю границу последовательности, то функцию, написанную в той задачке, можно прогнать для отладки поведения секундомера.




class Timing:
    def __init__(self, function_to_run):
        self.num_runs = 1000
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(
            "[Timing] \n Среднее время выполнения %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg
            )
        )
        return self.func_to_run(*args, **kwargs)


@Timing
def fibonacci(n=40000000 * 100 ^ (2 * 10000000000000)):
    n = int(n)

    def fibon(a, b, n, result):
        c = a + b
        result.append(c)
        if c < n:
            fibon(b, c, n, result)
        return result

    return fibon(0, 1, n, [])


print("Результат работы: \n" + str(fibonacci()))
