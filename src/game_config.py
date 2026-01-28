"""
Game configuration class - demonstrates class attributes
"""


class GameConfig:
    """Game configuration class - demonstrates class attributes"""
    GRID_SIZE = 20
    CELL_SIZE = 25
    INITIAL_GAME_SPEED = 600  # Start slower (higher value = slower)
    MIN_GAME_SPEED = 50  # Fastest speed
    SPEED_DECREASE = 5  # Speed up by this amount each food eaten
    INITIAL_SNAKE_LENGTH = 3
    
    # Color configuration
    SNAKE_HEAD_COLOR = "#2ecc71"
    SNAKE_BODY_COLOR = "#27ae60"
    SNAKE_OUTLINE_COLOR = "#229954"
    FOOD_COLOR = "#e74c3c"
    FOOD_OUTLINE_COLOR = "#c0392b"
    GRID_COLOR = "#2c3e50"
    BG_COLOR = "#34495e"
