# Tic-Tac-Toe Game

A complete Python implementation of the classic Tic-Tac-Toe game with both CLI and GUI interfaces.

## Features

- **Dual Interface**: Play with either a beautiful GUI or command-line interface
- **Smart Game Logic**: Complete win detection and game state management
- **Game Statistics**: Track wins for both players and ties (GUI mode)
- **Modern Design**: Clean, user-friendly interface with color-coded players
- **Error Handling**: Robust input validation and error handling

## How to Play

### GUI Mode (Default)
Run the game with the graphical interface:
```bash
python tic_tac_toe.py
```

### CLI Mode
Run the game in command-line mode:
```bash
python tic_tac_toe.py --cli
```

## Game Rules

1. The game is played on a 3x3 grid
2. Players take turns placing X's and O's
3. The first player to get 3 marks in a row (horizontal, vertical, or diagonal) wins
4. If all 9 squares are filled and no player has 3 in a row, the game is a tie

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python installations)

No additional dependencies required!
