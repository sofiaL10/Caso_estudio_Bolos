from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Game:
    def __init__(self):
        self.frames = [Frame() for _ in range(10)]

    def roll(self, pins: int):
        pass

    def score(self) -> int:
        puntaje_total = 0
        for i, frame in enumerate(self.frames):
            puntaje_total += frame.puntaje_frame()

            if frame.es_strike():
                if i < 9:
                    siguiente_frame = self.frames[i + 1]
                    if siguiente_frame.is_strike() and i < 8:
                        siguiente_siguiente_frame = self.frames[i + 2]
                        puntaje_total += siguiente_frame.score() + siguiente_siguiente_frame.rolls[0]
                    else:
                        puntaje_total += siguiente_frame.score()
                elif i == 9:
                    puntaje_total += sum(frame.rolls[1:])

            elif frame.es_spare():
                if i < 9:
                    siguiente_frame = self.frames[i + 1]
                    puntaje_total += siguiente_frame.rolls[0]

        return puntaje_total


class Roll:
    def __init__(self, pins: int):
        self.pins: int = pins


class Frame(ABC):
    def __init__(self):
        self.rolls = []

    @abstractmethod
    def add_roll(self, pins: int):
        pass

    @abstractmethod
    def score(self) -> int:
        return sum(self.rolls)

    def is_spare(self) -> bool:
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def is_strike(self) -> bool:
        return len(self.rolls) == 1 and self.rolls[0] == 10


class NormalFrame(Frame):
    def add_roll(self, pins: int):
        pass

    def score(self) -> int:
        pass


class TenthFrame(Frame):
    def add_roll(self, pins: int):
        pass

    def score(self) -> int:
        pass







