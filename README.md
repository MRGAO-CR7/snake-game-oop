[中文版](README_CN.md) | [English](README.md)

# Snake Game - Object-Oriented Programming Version

## 📋 Introduction

This is a Snake game implemented using **object-oriented programming**. The code uses classes and objects, demonstrating the advantages and features of OOP.

## 🎯 Programming Style Features

### 1. Using Classes and Objects
```python
class Snake:
    def __init__(self, start_pos, initial_length):
        self.body = [start_pos]
        self.direction = Direction.RIGHT
    
    def move(self):
        # Movement logic
```

### 2. Encapsulation
- ✅ Data and operations encapsulated in classes
- ✅ Access and modify state through methods
- ✅ Hide internal implementation details

### 3. Separation of Concerns
- `Snake` class: Manages snake state and behavior
- `Food` class: Manages food generation and position
- `GameBoard` class: Manages game state
- `GameRenderer` class: Handles rendering
- `SnakeGameGUI` class: Manages GUI interface

## 📁 Code Structure

```
snake-game-oop/
├── main.py                 # Main entry point (directly imports and runs SnakeGameGUI)
└── src/                    # Source code folder
    ├── __init__.py         # Package initialization file
    ├── direction.py        # Direction enum
    ├── point.py            # Point dataclass
    ├── game_config.py      # GameConfig configuration class
    │   ├── Speed configuration (INITIAL_GAME_SPEED, MIN_GAME_SPEED, etc.)
    │   └── Color configuration
    ├── snake.py            # Snake class - Manages snake state and behavior
    ├── food.py             # Food class - Manages apple (random position generation)
    ├── game_board.py       # GameBoard game logic class
    │   ├── update() - Update game state (speed increase logic)
    │   ├── current_speed - Dynamic speed management
    │   └── reset() - Reset game (reset speed)
    ├── game_renderer.py    # GameRenderer renderer class
    │   ├── draw_apple() - Draw apple emoji
    │   ├── draw_snake_head() - Draw snake head (with eyes)
    │   ├── draw_snake_body() - Draw snake body
    │   ├── draw_snake_tail() - Draw snake tail
    │   └── draw_snake() - Draw complete snake
    └── snake_game_gui.py   # SnakeGameGUI GUI main class
        ├── _create_widgets() - Create interface (optimized button style)
        └── _game_loop() - Use dynamic speed
```

**Modular Design Advantages**:
- ✅ Single responsibility per file
- ✅ Easy to maintain and test
- ✅ Strong code reusability
- ✅ Clear dependency relationships

See `STRUCTURE.md` for detailed information.

## 🔧 Environment Setup

### macOS
1. **Install Python 3.11+** (if not already installed):
   ```bash
   brew install python3
   ```

2. **Install tkinter** (required for GUI):
   ```bash
   brew install python-tk
   ```

3. **Verify installation**:
   ```bash
   python3 -c "import tkinter; print('tkinter is ready!')"
   ```

### Windows
1. **Install Python 3.11+** from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation
   - ✅ tkinter is included by default with Python on Windows

2. **Verify installation**:
   ```cmd
   python -c "import tkinter; print('tkinter is ready!')"
   ```

## 🎮 How to Run

```bash
python3 main.py
```

Or:

```bash
cd snake-game-oop
python3 main.py
```

## ⚙️ Game Controls

- **Arrow Keys** or **WASD**: Control snake movement
- **Spacebar**: Pause/Resume
- **Restart Button**: Start new game

## 🎮 Game Features

### Speed System
- **Initial Speed**: 600ms (very slow, suitable for beginners)
- **Speed Increase**: Each apple 🍎 eaten increases speed (decreases delay by 5ms)
- **Maximum Speed**: 50ms (ultimate challenge)
- **Restart**: Speed resets to initial value

### Graphics Design
- **Apple**: Red apple emoji 🍎, clear and eye-catching
- **Snake Head**: Green circle with eyes (shows direction)
- **Snake Body**: Green circles with gradient effect
- **Snake Tail**: Smaller green circle, clearly distinguishable
- **All Snake Parts**: Unified green color scheme

### Apple Generation
- **Random Position**: Uses `random.randint()` to randomly select position each time
- **Smart Avoidance**: Ensures apples don't spawn on snake body
- **Instant Refresh**: Generates new position immediately after eating

### UI Optimization
- **Button Style**: Light gray background + dark text, clear and readable
- **Visual Feedback**: Buttons have 3D effect (raised relief)
- **Beautiful Interface**: Unified color scheme

## 💡 Advantages of Object-Oriented Programming

### ✅ Advantages

1. **Encapsulation**
   - Data and operations encapsulated together
   - Hide internal implementation details
   - Provide clear interfaces

2. **Maintainability**
   - Clear code organization
   - Easy to understand and modify
   - Clear separation of concerns

3. **Extensibility**
   - Easy to add new features
   - Can inherit and extend classes
   - Support polymorphism

4. **Reusability**
   - Classes can be reused in other projects
   - Reduce code duplication

5. **Type Safety**
   - Use type hints
   - Enum types avoid magic values
   - Data classes provide structured data

## 📚 Learning Points

### 1. Class Design
```python
class Snake:
    def __init__(self, start_pos, initial_length):
        # Initialization
    def move(self):
        # Behavior
    def check_collision(self):
        # Behavior
```

### 2. Enum Types
```python
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
```

### 3. Data Classes
```python
@dataclass
class Point:
    x: int
    y: int
```

### 4. Type Hints
```python
def move(self) -> None:
def get_head(self) -> Point:
```

### 5. Separation of Concerns
- Each class handles one responsibility
- Classes interact through interfaces
- Reduce coupling

## 🔄 Compare with Functional Version

Check out `../snake-game-functional/` to understand the differences between the two programming styles!

## 🎓 Advanced Features

### 1. Operator Overloading
```python
def __add__(self, other):
    # Overload + operator
```

### 2. Class Methods
```python
@classmethod
def generate_random(cls, ...):
    # Class method
```

### 3. Property Access
```python
@property
def position(self):
    return self._position
```

## 💻 Code Examples

### Create Snake Object
```python
snake = Snake(Point(10, 10), initial_length=3)
snake.move()
snake.grow()
```

### Create Game Board
```python
board = GameBoard(width=20, height=20)
board.update()
state = board.get_state()
```

### Use Renderer
```python
renderer = GameRenderer(canvas, cell_size=25)
renderer.draw_snake(snake.get_body())
renderer.draw_food(food.get_position())
```

## 🚀 Extension Suggestions

1. **Add New Features**
   - ~~Different difficulty levels~~ ✅ Implemented: Speed increases with score
   - Obstacles
   - Special food (speed boost, slow down)

2. **Improve Code**
   - Add unit tests
   - Use design patterns (Observer pattern, etc.)
   - Add configuration files

3. **Learn New Concepts**
   - Inheritance and polymorphism
   - Abstract base classes
   - Design patterns
