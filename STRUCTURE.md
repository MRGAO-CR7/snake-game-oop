# 项目结构说明 / Project Structure

## 📁 文件组织

面向对象版本已拆分为多个文件，每个类/枚举/数据类都有独立的文件：

```
oop_version/
├── main.py                 # 主入口文件（直接导入并运行SnakeGameGUI）
├── src/                    # 源代码文件夹
│   ├── __init__.py         # 包初始化文件
│   ├── direction.py        # Direction 枚举
│   ├── point.py            # Point 数据类
│   ├── game_config.py      # GameConfig 配置类
│   ├── snake.py            # Snake 类
│   ├── food.py             # Food 类
│   ├── game_board.py       # GameBoard 游戏逻辑类
│   ├── game_renderer.py    # GameRenderer 渲染器类
│   └── snake_game_gui.py   # SnakeGameGUI GUI主类
├── README_CN.md            # 中文说明
├── README_EN.md            # English README
└── STRUCTURE.md            # 项目结构说明（本文件）
```

## 🔗 文件依赖关系

```
main.py (oop_version/)
  └── src.snake_game_gui
        ├── src.direction
        ├── src.game_board
        │     ├── src.point
        │     ├── src.snake
        │     │     ├── src.point
        │     │     └── src.direction
        │     ├── src.food
        │     │     └── src.point
        │     └── src.game_config
        ├── src.game_renderer
        │     ├── src.point
        │     ├── src.direction
        │     └── src.game_config
        └── src.game_config
```

**导入方式**：
- `src/` 文件夹内的文件使用**相对导入**（`from .module import Class`）
- `main.py` 使用**绝对导入**（`from src.module import Class`）

## 📝 文件说明

### `main.py` (oop_version目录下)
- **作用**：程序入口点
- **内容**：直接导入 `SnakeGameGUI` 并创建实例运行
- **运行方式**：`python3 main.py`
- **导入方式**：`from src.snake_game_gui import SnakeGameGUI`

### `src/direction.py`
- **作用**：定义方向枚举
- **内容**：`Direction` 枚举类（UP, DOWN, LEFT, RIGHT）
- **依赖**：无
- **导入方式**：`from .direction import Direction`（相对导入）

### `src/point.py`
- **作用**：定义坐标点数据类
- **内容**：`Point` 数据类，支持运算符重载
- **依赖**：`src/direction.py`
- **导入方式**：`from .point import Point`（相对导入）

### `src/game_config.py`
- **作用**：游戏配置常量
- **内容**：`GameConfig` 类，包含所有配置参数
- **依赖**：无
- **导入方式**：`from .game_config import GameConfig`（相对导入）

### `src/snake.py`
- **作用**：蛇类，管理蛇的状态和行为
- **内容**：`Snake` 类
- **依赖**：`src/point.py`, `src/direction.py`
- **导入方式**：`from .snake import Snake`（相对导入）

### `src/food.py`
- **作用**：食物类，管理苹果的生成和位置
- **内容**：`Food` 类
- **依赖**：`src/point.py`
- **导入方式**：`from .food import Food`（相对导入）

### `src/game_board.py`
- **作用**：游戏板类，管理游戏状态
- **内容**：`GameBoard` 类
- **依赖**：`src/point.py`, `src/snake.py`, `src/food.py`, `src/game_config.py`
- **导入方式**：`from .game_board import GameBoard`（相对导入）

### `src/game_renderer.py`
- **作用**：渲染器类，负责绘制游戏画面
- **内容**：`GameRenderer` 类
- **依赖**：`src/point.py`, `src/direction.py`, `src/game_config.py`
- **导入方式**：`from .game_renderer import GameRenderer`（相对导入）

### `src/snake_game_gui.py`
- **作用**：GUI主类，管理整个图形界面
- **内容**：`SnakeGameGUI` 类
- **依赖**：`src/direction.py`, `src/game_board.py`, `src/game_renderer.py`, `src/game_config.py`
- **导入方式**：`from .snake_game_gui import SnakeGameGUI`（相对导入）

## 🚀 运行方式

```bash
cd oop_version
python3 main.py
```

**注意**：所有源代码文件都在 `src/` 文件夹中，使用相对导入（`from .module import Class`）。

## 💡 模块化设计的优势

1. **职责分离**：每个文件只负责一个类/功能
2. **易于维护**：修改某个类只需编辑对应文件
3. **易于测试**：可以单独测试每个模块
4. **代码复用**：其他项目可以轻松导入单个类
5. **清晰的依赖关系**：通过导入语句明确显示依赖

## 📚 导入示例

如果需要在其他项目中使用这些类：

```python
# 从src包导入
from src.direction import Direction
from src.point import Point
from src.snake import Snake

# 使用
snake = Snake(Point(10, 10))
snake.change_direction(Direction.RIGHT)
```

**包结构**：
- `src/` 文件夹是一个Python包（包含 `__init__.py`）
- 所有模块使用相对导入（`from .module import Class`）
- 外部导入使用绝对导入（`from src.module import Class`）
