import time

class TimerError(Exception):

class Timer:
        def __init__(self):
            self._start_time = None

        def start(self):
            if self._start_time is not None:
                raise TimerError

            self._start_time =  time.perf_counter()

        def stop(self):
            if self._start_time is None:
                raise TimerError

            elapsed_time = time.perf_counter() - self._start_time
            self._start_time = None

            with open("CzasDzialania.txt", "r") as work_time_file:
                work_time = work_time_file.readlines()

                work_time += elapsed_time

                print(f"Ta sesja trwa: {elapsed_time:0.4f} seconds")
                print(f"W sumie program dziala juz: {work_time:0.4f} seconds")

            work_time_file.close()
