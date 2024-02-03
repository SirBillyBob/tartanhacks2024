from __future__ import annotations
import math
from typing import *
from cmu_graphics import almostEqual


class Vector2:
    
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y
    
    @property
    def mag(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def angle(self) -> float:
        return math.atan(-self.x / self.y)

    @property
    def float(self) -> Vector2:
        return Vector2(float(self.x), float(self.y))

    def copy(self) -> Vector2:
        return Vector2(self.x, self.y)

    def normalize(self) -> None:
        self.x /= self.mag
        self.y /= self.mag

    def rotatedRight(self) -> Vector2:  # TODO: use this func in trig calcs
        return Vector2(self.y, -self.x)

    def rotatedLeft(self) -> Vector2:
        return -self.rotatedRight()

    def __getitem__(self, key: int) -> Union[int, float]:
        return (self.x, self.y)[key]

    def __setitem__(self, key, val):
        setattr(self, 'xy'[key], val)

    def __iter__(self) -> Generator:
        return (self.__dict__[item] for item in 'xy')

    def __repr__(self) -> str:
        return 'Vector ' + chr(10216) + f'{self.x}, {self.y}' + chr(10217)

    def __add__(self, v: Vector2) -> Vector2:
        try:
            return Vector2(self.x + v.x, self.y + v.y)
        except AttributeError:
            raise NotImplementedError(
                ('Addition not supported between type Vector2 and '
                 f'type {type(v)}')
            )
    
    def __sub__(self, v: Vector2) -> Vector2:
        try:
            return Vector2(self.x - v.x, self.y - v.y)
        except AttributeError:
            raise NotImplementedError(
                ('Subtraction not supported between type Vector2 and '
                 f'type {type(v)}')
            )

    def __mul__(self, val: Union[float, int]) -> Vector2:
        if isinstance(val, float) or isinstance(val, int):
            return Vector2(self.x * val, self.y * val)
        else:
            raise NotImplementedError(
                'Multiplication is not supported between type Vector2 and '
                f'type {type(val)}'
            )
    
    def __rmul__(self, val: Union[float, int]) -> Vector2:
        return self * val

    def __truediv__(self, val: Union[float, int]) -> Vector2:
        return self * (1 / val)

    def __neg__(self) -> Vector2:
        return Vector2(-self.x, -self.y)

    def __mod__(self, v: Vector2) -> Vector2:
        return Vector2(self.x % v.x, self.y % v.y)

    def __floordiv__(self, val: Union[float, int, Vector2]
                     ) -> Union[float, int, Vector2]:
        if isinstance(val, float) or isinstance(val, int):
            return Vector2(self.x // val, self.y // val)

        elif isinstance(val, Vector2):
            return Vector2(self.x // val.x, self.y // val.y)

    def __eq__(self, val: Vector2) -> bool:
        if almostEqual(self.x, val.x) and almostEqual(self.y, val.y):
            return True
        else:
            return False
    
    def __ne__(self, val: Vector2) -> bool:
        if self == val:
            return False
        else:
            return True


def dot(v1: Vector2, v2: Vector2) -> float:
    return v1.x * v2.x + v1.y * v2.y

def cross(v1: Vector2, v2: Vector2) -> float:
    return v1.x * v2.y - v1.y * v2.x

def dist(v1: Vector2, v2: Vector2 = Vector2(0, 0)) -> float:
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)
