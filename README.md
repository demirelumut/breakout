# 🎮 Breakout Game

This is a simple implementation of the classic **Breakout** game, written in Python using the **Pygame** library. The goal of the game is to control a paddle and bounce a ball to break all the bricks on the screen without letting the ball fall off the screen.

## 🚀 Features

- 🕹️ **Paddle** controlled by the mouse to bounce a ball.
- 🎨 **Colored bricks** that break when hit by the ball.
- ⚡ **Ball movement** with speed variation and bouncing behavior.
- 💔 **Life counter**, with the game ending when all lives are lost.
- 🏆 **Game win** when all bricks are cleared.
- 🕹️ **Game over** screen when the player loses all lives.

## 🎮 Game Controls

- **Mouse Movement**: Move the paddle left and right to bounce the ball and break the bricks.

## ⚙️ Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/breakout-game.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd breakout-game
    ```

3. Install the required Python libraries using `pip`:
    ```bash
    pip install pygame
    ```

## 🏁 How to Play

1. Run the game:
    ```bash
    python breakout.py
    ```

2. The game window will open. Use your mouse to move the paddle and bounce the ball to break the bricks.

3. The goal is to break all the bricks. If the ball falls below the paddle, you lose a life. The game ends when you run out of lives or clear all the bricks.

## 💡 Game Logic

- **Ball Movement**: The ball moves at a random speed in both the x and y directions. It bounces off walls, the paddle, and the bricks.
  
- **Paddle**: The paddle is controlled by the mouse. It is constrained within the boundaries of the screen.

- **Bricks**: There are 6 rows and 11 columns of bricks. Each brick has a different color. When the ball collides with a brick, the brick disappears, and the ball bounces back.

- **Lives**: The player starts with 3 lives. When the ball hits the bottom of the screen, a life is lost. The game ends when the player runs out of lives.

- **Win Condition**: The player wins the game by breaking all the bricks.

## 📸 Screenshots

Add some screenshots here to showcase your game in action.

## 📋 Dependencies

- Python 3.x
- Pygame

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- This game is built using the Pygame library, which provides excellent tools for creating 2D games in Python.
- Thanks to all the contributors and resources available for learning game development with Pygame.
