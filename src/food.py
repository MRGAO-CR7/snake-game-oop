"""
Food class - demonstrates single responsibility principle
"""

from typing import List
import random
from .point import Point


class Food:
    """Food class - demonstrates single responsibility principle"""
    
    def __init__(self, position: Point):
        self.position = position
    
    @classmethod
    def generate_random(cls, width: int, height: int, snake_body: List[Point]) -> 'Food':
        """Generate random food position (apple) - random position not on snake"""
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pos = Point(x, y)
            if pos not in snake_body:
                return cls(pos)  # Random apple position
    
    def get_position(self) -> Point:
        """Get food position"""
        return self.position
