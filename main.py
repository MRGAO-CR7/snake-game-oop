"""
Main entry point for Snake Game - Object-Oriented Version
"""

from src.snake_game_gui import SnakeGameGUI


def main():
    """Main function"""
    app = SnakeGameGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
