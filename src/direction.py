"""
Direction enum - demonstrates enum usage
"""

from enum import Enum


class Direction(Enum):
    """Direction enum - demonstrates enum usage"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    
    @classmethod
    def opposite(cls, direction):
        """Get opposite direction"""
        opposites = {
            cls.UP: cls.DOWN,
            cls.DOWN: cls.UP,
            cls.LEFT: cls.RIGHT,
            cls.RIGHT: cls.LEFT
        }
        return opposites.get(direction)
