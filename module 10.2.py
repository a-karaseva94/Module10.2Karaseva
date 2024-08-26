# Задача "За честь и отвагу!":

from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        warriors = 100
        days = 0
        print(f'{self.name}, на нас напали!\n')
        while warriors > 0:
            if warriors > self.power:
                warriors = warriors - self.power
            elif warriors <= self.power:
                warriors = 0
            time.sleep(1)
            days += 1
            print(f'{self.name} сражается {days} день(дней,дня), осталось {warriors} воинов(а,ов).\n')
        print(f'{self.name} одержал победу спустя {days} день(дней,дня)!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
