"""
Snake class - demonstrates encapsulation and state management
"""

from typing import List
from .point import Point
from .direction import Direction


class Snake:
    """Snake class - demonstrates encapsulation and state management"""
    
    def __init__(self, start_pos: Point, initial_length: int = 3):
        """Initialize snake"""
        self.body: List[Point] = [start_pos]
        self.direction: Direction = Direction.RIGHT
        self.next_direction: Direction = Direction.RIGHT
        self.grow_pending: int = initial_length - 1
    
    def change_direction(self, new_direction: Direction):
        """Change direction (prevents reverse movement)"""
        if Direction.opposite(new_direction) != self.direction:
            self.next_direction = new_direction
    
    def move(self):
        """Move snake"""
        self.direction = self.next_direction
        new_head = self.body[0] + self.direction
        
        self.body.insert(0, new_head)
        
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def grow(self):
        """Make snake grow"""
        self.grow_pending += 1
    
    def check_collision(self, width: int, height: int) -> bool:
        """Check collision"""
        head = self.body[0]
        
        # Check boundaries
        if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height:
            return True
        
        # Check if hit itself
        if head in self.body[1:]:
            return True
        
        return False
    
    def get_head(self) -> Point:
        """Get head position"""
        return self.body[0]
    
    def get_body(self) -> List[Point]:
        """Get body position list"""
        return self.body.copy()
