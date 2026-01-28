"""
Game board class - demonstrates game state management
"""

from .point import Point
from .snake import Snake
from .food import Food
from .game_config import GameConfig


class GameBoard:
    """Game board class - demonstrates game state management"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.snake = Snake(
            Point(width // 2, height // 2),
            GameConfig.INITIAL_SNAKE_LENGTH
        )
        self.food = Food.generate_random(
            width, height, self.snake.get_body()  # Random apple position
        )
        self.score = 0
        self.game_over = False
        self.current_speed = GameConfig.INITIAL_GAME_SPEED
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        self.snake.move()
        
        # Check collision
        if self.snake.check_collision(self.width, self.height):
            self.game_over = True
            return
        
        # Check if food (apple) is eaten
        if self.snake.get_head() == self.food.position:
            self.snake.grow()
            self.score += 1  # Score increases by 1 for each apple
            self.food = Food.generate_random(
                self.width,
                self.height,
                self.snake.get_body()  # Generate new random apple position
            )
            # Increase speed (decrease delay) each time food is eaten
            self.current_speed = max(
                GameConfig.MIN_GAME_SPEED,
                self.current_speed - GameConfig.SPEED_DECREASE
            )
    
    def get_state(self) -> dict:
        """Get game state"""
        return {
            'snake_body': self.snake.get_body(),
            'food_pos': self.food.position,
            'score': self.score,
            'game_over': self.game_over,
            'snake_direction': self.snake.direction
        }
    
    def reset(self):
        """Reset game"""
        self.snake = Snake(
            Point(self.width // 2, self.height // 2),
            GameConfig.INITIAL_SNAKE_LENGTH
        )
        self.food = Food.generate_random(
            self.width, self.height, self.snake.get_body()  # Random apple position
        )
        self.score = 0
        self.game_over = False
        self.current_speed = GameConfig.INITIAL_GAME_SPEED  # Reset speed
