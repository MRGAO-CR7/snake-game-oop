"""
Snake game GUI main class - demonstrates GUI application architecture
"""

import tkinter as tk
from tkinter import messagebox
from .direction import Direction
from .game_board import GameBoard
from .game_renderer import GameRenderer
from .game_config import GameConfig


class SnakeGameGUI(tk.Tk):
    """Snake game GUI main class - demonstrates GUI application architecture"""
    
    def __init__(self):
        super().__init__()
        self.title("Snake Game - Object-Oriented Version")
        self.geometry("600x700")
        self.resizable(False, False)
        
        # Create game components
        self.board = GameBoard(
            GameConfig.GRID_SIZE,
            GameConfig.GRID_SIZE
        )
        
        # Create renderer
        self.renderer = None  # Will be initialized after canvas creation
        
        # Game state
        self.paused = False
        
        # Bind keyboard events
        self.bind("<KeyPress>", self._on_key_press)
        self.focus_set()
        
        self._create_widgets()
        self._draw_game()
        self._game_loop()
    
    def _create_widgets(self):
        """Create interface components"""
        # Title and score
        header_frame = tk.Frame(self, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🐍 Snake Game (OOP)",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=10)
        
        self.score_label = tk.Label(
            header_frame,
            text="Score: 0",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.score_label.pack()
        
        # Game canvas
        canvas_width = GameConfig.GRID_SIZE * GameConfig.CELL_SIZE
        canvas_height = GameConfig.GRID_SIZE * GameConfig.CELL_SIZE
        
        self.canvas = tk.Canvas(
            self,
            width=canvas_width,
            height=canvas_height,
            bg=GameConfig.BG_COLOR,
            highlightthickness=2,
            highlightbackground="#2c3e50"
        )
        self.canvas.pack(pady=20)
        
        # Initialize renderer
        self.renderer = GameRenderer(self.canvas, GameConfig.CELL_SIZE)
        
        # Control buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        
        restart_btn = tk.Button(
            button_frame,
            text="Restart",
            command=self._restart_game,
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",  # Light gray background
            fg="#2c3e50",  # Dark text for better visibility
            width=12,
            height=2,
            cursor="hand2",
            relief=tk.RAISED,
            bd=2
        )
        restart_btn.pack(side=tk.LEFT, padx=5)
        
        pause_btn = tk.Button(
            button_frame,
            text="Pause/Resume",
            command=self._toggle_pause,
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",  # Light gray background
            fg="#2c3e50",  # Dark text for better visibility
            width=12,
            height=2,
            cursor="hand2",
            relief=tk.RAISED,
            bd=2
        )
        pause_btn.pack(side=tk.LEFT, padx=5)
        
        # Instructions
        info_label = tk.Label(
            self,
            text="Use arrow keys or WASD to control the snake",
            font=("Arial", 10),
            fg="#7f8c8d"
        )
        info_label.pack(pady=5)
    
    def _on_key_press(self, event):
        """Handle keyboard input"""
        key = event.keysym.lower()
        
        key_mapping = {
            'up': Direction.UP,
            'w': Direction.UP,
            'down': Direction.DOWN,
            's': Direction.DOWN,
            'left': Direction.LEFT,
            'a': Direction.LEFT,
            'right': Direction.RIGHT,
            'd': Direction.RIGHT
        }
        
        if key in key_mapping:
            self.board.snake.change_direction(key_mapping[key])
        elif key == 'space':
            self._toggle_pause()
    
    def _draw_game(self):
        """Draw game screen"""
        self.canvas.delete("all")
        
        state = self.board.get_state()
        
        # Draw grid
        self.renderer.draw_grid(GameConfig.GRID_SIZE)
        
        # Draw apple (red apple emoji)
        self.renderer.draw_food(state['food_pos'])
        
        # Draw snake (green with head, body, tail)
        self.renderer.draw_snake(state['snake_body'], state['snake_direction'])
        
        # Update score display
        self.score_label.config(text=f"Score: {state['score']}")
        
        # Game over message
        if state['game_over']:
            self.renderer.draw_game_over(
                state['score'],
                GameConfig.GRID_SIZE
            )
    
    def _game_loop(self):
        """Main game loop"""
        if not self.paused and not self.board.game_over:
            self.board.update()
            self._draw_game()
            
            if self.board.game_over:
                messagebox.showinfo(
                    "Game Over",
                    f"Game Over!\nFinal Score: {self.board.score}\n\n"
                    f"Click 'Restart' to start a new game"
                )
        
        # Use dynamic speed based on score
        self.after(self.board.current_speed, self._game_loop)
    
    def _restart_game(self):
        """Restart game"""
        self.board.reset()
        self.paused = False
        self._draw_game()
    
    def _toggle_pause(self):
        """Toggle pause/resume"""
        if not self.board.game_over:
            self.paused = not self.paused
