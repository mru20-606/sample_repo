#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A complete implementation with both CLI and GUI interfaces.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import sys
from typing import Optional, List, Tuple

class TicTacToeGame:
    """Core game logic for Tic-Tac-Toe"""
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def make_move(self, row: int, col: int) -> bool:
        """Make a move on the board"""
        if self.game_over or self.board[row][col] != ' ':
            return False
            
        self.board[row][col] = self.current_player
        
        if self.check_winner():
            self.game_over = True
            self.winner = self.current_player
        elif self.is_board_full():
            self.game_over = True
            self.winner = 'Tie'
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            
        return True
        
    def check_winner(self) -> bool:
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
                
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
            
        return False
        
    def is_board_full(self) -> bool:
        """Check if the board is full"""
        return all(cell != ' ' for row in self.board for cell in row)
        
    def get_empty_cells(self) -> List[Tuple[int, int]]:
        """Get list of empty cells"""
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']


class TicTacToeCLI:
    """Command Line Interface for Tic-Tac-Toe"""
    
    def __init__(self):
        self.game = TicTacToeGame()
        
    def print_board(self):
        """Print the current board state"""
        print("\n   0   1   2")
        for i, row in enumerate(self.game.board):
            print(f"{i}  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("  ---|---|---")
        print()
        
    def get_move(self) -> Tuple[int, int]:
        """Get move input from player"""
        while True:
            try:
                move = input(f"Player {self.game.current_player}, enter your move (row,col): ")
                row, col = map(int, move.split(','))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Invalid input! Please enter row and column between 0-2.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter in format: row,col (e.g., 1,2)")
                
    def play(self):
        """Main game loop for CLI"""
        print("Welcome to Tic-Tac-Toe!")
        print("Enter moves as: row,col (e.g., 1,2)")
        
        while not self.game.game_over:
            self.print_board()
            row, col = self.get_move()
            
            if not self.game.make_move(row, col):
                print("Invalid move! Cell already occupied.")
                continue
                
        self.print_board()
        
        if self.game.winner == 'Tie':
            print("It's a tie!")
        else:
            print(f"Player {self.game.winner} wins!")
            
        if input("Play again? (y/n): ").lower() == 'y':
            self.game.reset_game()
            self.play()


class TicTacToeGUI:
    """Graphical User Interface for Tic-Tac-Toe using tkinter"""
    
    def __init__(self):
        self.game = TicTacToeGame()
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Style configuration
        self.root.configure(bg='#2c3e50')
        
        # Game statistics
        self.stats = {'X': 0, 'O': 0, 'Tie': 0}
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="TIC-TAC-TOE", 
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=10)
        
        # Current player display
        self.player_label = tk.Label(
            self.root,
            text=f"Current Player: {self.game.current_player}",
            font=('Arial', 14),
            bg='#2c3e50',
            fg='#3498db'
        )
        self.player_label.pack(pady=5)
        
        # Game board frame
        board_frame = tk.Frame(self.root, bg='#2c3e50')
        board_frame.pack(pady=20)
        
        # Create buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text=' ',
                    font=('Arial', 24, 'bold'),
                    width=4,
                    height=2,
                    bg='#ecf0f1',
                    fg='#2c3e50',
                    command=lambda r=i, c=j: self.make_move(r, c),
                    relief='raised',
                    bd=2
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)
            
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg='#2c3e50')
        control_frame.pack(pady=20)
        
        # Reset button
        reset_button = tk.Button(
            control_frame,
            text="New Game",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            command=self.reset_game,
            padx=20,
            pady=5
        )
        reset_button.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_button = tk.Button(
            control_frame,
            text="Quit",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            command=self.root.quit,
            padx=20,
            pady=5
        )
        quit_button.pack(side=tk.LEFT, padx=10)
        
        # Statistics display
        self.stats_label = tk.Label(
            self.root,
            text=self.get_stats_text(),
            font=('Arial', 10),
            bg='#2c3e50',
            fg='#95a5a6'
        )
        self.stats_label.pack(pady=10)
        
    def get_stats_text(self) -> str:
        """Get formatted statistics text"""
        return f"Wins - X: {self.stats['X']} | O: {self.stats['O']} | Ties: {self.stats['Tie']}"
        
    def make_move(self, row: int, col: int):
        """Handle button click for making a move"""
        if self.game.make_move(row, col):
            # Update button
            self.buttons[row][col].config(
                text=self.game.board[row][col],
                state='disabled',
                bg='#bdc3c7' if self.game.board[row][col] == 'X' else '#f39c12',
                fg='white'
            )
            
            if self.game.game_over:
                self.end_game()
            else:
                # Update current player display
                self.player_label.config(text=f"Current Player: {self.game.current_player}")
                
    def end_game(self):
        """Handle game end"""
        # Disable all buttons
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
                
        # Update statistics
        if self.game.winner and self.game.winner != 'Tie':
            self.stats[self.game.winner] += 1
        elif self.game.winner == 'Tie':
            self.stats['Tie'] += 1
            
        self.stats_label.config(text=self.get_stats_text())
        
        # Show result
        if self.game.winner == 'Tie':
            messagebox.showinfo("Game Over", "It's a tie!")
            self.player_label.config(text="Game Over - Tie!")
        else:
            messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
            self.player_label.config(text=f"Game Over - Player {self.game.winner} wins!")
            
    def reset_game(self):
        """Reset the game"""
        self.game.reset_game()
        
        # Reset all buttons
        for row in self.buttons:
            for button in row:
                button.config(
                    text=' ',
                    state='normal',
                    bg='#ecf0f1',
                    fg='#2c3e50'
                )
                
        # Reset player label
        self.player_label.config(text=f"Current Player: {self.game.current_player}")
        
    def run(self):
        """Start the GUI"""
        self.root.mainloop()


def main():
    """Main function to choose between CLI and GUI"""
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        # Run CLI version
        game = TicTacToeCLI()
        game.play()
    else:
        # Run GUI version (default)
        try:
            game = TicTacToeGUI()
            game.run()
        except tk.TclError:
            print("GUI not available. Running CLI version...")
            game = TicTacToeCLI()
            game.play()


if __name__ == "__main__":
    main()