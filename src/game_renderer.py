"""
Game renderer class - demonstrates separation of concerns
"""

import tkinter as tk
from typing import List
from .point import Point
from .direction import Direction
from .game_config import GameConfig


class GameRenderer:
    """Game renderer class - demonstrates separation of concerns"""
    
    def __init__(self, canvas: tk.Canvas, cell_size: int):
        self.canvas = canvas
        self.cell_size = cell_size
    
    def draw_grid(self, grid_size: int):
        """Draw grid lines"""
        for i in range(grid_size + 1):
            x = i * self.cell_size
            self.canvas.create_line(
                x, 0, x, grid_size * self.cell_size,
                fill=GameConfig.GRID_COLOR, width=1
            )
            y = i * self.cell_size
            self.canvas.create_line(
                0, y, grid_size * self.cell_size, y,
                fill=GameConfig.GRID_COLOR, width=1
            )
    
    def draw_apple(self, point: Point):
        """Draw apple (red apple emoji)"""
        center_x = point.x * self.cell_size + self.cell_size // 2
        center_y = point.y * self.cell_size + self.cell_size // 2
        self.canvas.create_text(
            center_x, center_y,
            text="🍎",
            font=("Arial", self.cell_size - 4)
        )
    
    def draw_snake_head(self, point: Point, direction: Direction):
        """Draw snake head (green with direction)"""
        x1 = point.x * self.cell_size + 2
        y1 = point.y * self.cell_size + 2
        x2 = (point.x + 1) * self.cell_size - 2
        y2 = (point.y + 1) * self.cell_size - 2
        
        # Draw green rounded head
        self.canvas.create_oval(
            x1, y1, x2, y2,
            fill="#2ecc71",  # Green
            outline="#27ae60",
            width=2
        )
        
        # Draw eyes based on direction
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        eye_size = 3
        
        if direction == Direction.RIGHT:
            eye_x1, eye_x2 = center_x + 3, center_x + 3
            eye_y1, eye_y2 = center_y - 2, center_y + 2
        elif direction == Direction.LEFT:
            eye_x1, eye_x2 = center_x - 3, center_x - 3
            eye_y1, eye_y2 = center_y - 2, center_y + 2
        elif direction == Direction.UP:
            eye_x1, eye_x2 = center_x - 2, center_x + 2
            eye_y1, eye_y2 = center_y - 3, center_y - 3
        else:  # DOWN
            eye_x1, eye_x2 = center_x - 2, center_x + 2
            eye_y1, eye_y2 = center_y + 3, center_y + 3
        
        self.canvas.create_oval(eye_x1 - eye_size, eye_y1 - eye_size, eye_x1 + eye_size, eye_y1 + eye_size, fill="black")
        self.canvas.create_oval(eye_x2 - eye_size, eye_y2 - eye_size, eye_x2 + eye_size, eye_y2 + eye_size, fill="black")
    
    def draw_snake_body(self, point: Point):
        """Draw snake body (green rounded rectangle)"""
        x1 = point.x * self.cell_size + 2
        y1 = point.y * self.cell_size + 2
        x2 = (point.x + 1) * self.cell_size - 2
        y2 = (point.y + 1) * self.cell_size - 2
        
        self.canvas.create_oval(
            x1, y1, x2, y2,
            fill="#27ae60",  # Darker green
            outline="#229954",
            width=2
        )
    
    def draw_snake_tail(self, point: Point):
        """Draw snake tail (smaller green circle)"""
        x1 = point.x * self.cell_size + 4
        y1 = point.y * self.cell_size + 4
        x2 = (point.x + 1) * self.cell_size - 4
        y2 = (point.y + 1) * self.cell_size - 4
        
        self.canvas.create_oval(
            x1, y1, x2, y2,
            fill="#229954",  # Darkest green
            outline="#1e8449",
            width=2
        )
    
    def draw_snake(self, snake_body: List[Point], snake_direction: Direction):
        """Draw snake (green with head, body, tail)"""
        for i, pos in enumerate(snake_body):
            if i == 0:
                # Snake head (green with eyes)
                self.draw_snake_head(pos, snake_direction)
            elif i == len(snake_body) - 1:
                # Snake tail (smaller green circle)
                self.draw_snake_tail(pos)
            else:
                # Snake body (green circles)
                self.draw_snake_body(pos)
    
    def draw_food(self, food_pos: Point):
        """Draw food (red apple emoji)"""
        self.draw_apple(food_pos)
    
    def draw_game_over(self, score: int, grid_size: int):
        """Draw game over screen"""
        center_x = grid_size * self.cell_size // 2
        center_y = grid_size * self.cell_size // 2
        
        self.canvas.create_text(
            center_x,
            center_y - 20,
            text="Game Over!",
            font=("Arial", 24, "bold"),
            fill="#e74c3c"
        )
        self.canvas.create_text(
            center_x,
            center_y + 20,
            text=f"Final Score: {score}",
            font=("Arial", 16),
            fill="#ecf0f1"
        )
