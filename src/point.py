"""
Point data class - demonstrates dataclass usage
"""

from dataclasses import dataclass
from .direction import Direction


@dataclass
class Point:
    """Point data class - demonstrates dataclass usage"""
    x: int
    y: int
    
    def __eq__(self, other):
        """Overload equality operator"""
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        """Overload addition operator"""
        if isinstance(other, Direction):
            dx, dy = other.value
            return Point(self.x + dx, self.y + dy)
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
