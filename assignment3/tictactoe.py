# Task 6: More on Classes

class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        self.last_move = (row, column)
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        b = self.board_array

        for i in range(3):
            if b[i][0] != " " and b[i][0] == b[i][1] == b[i][2]:
                return (True, f"{b[i][0]} has won")

        for j in range(3):
            if b[0][j] != " " and b[0][j] == b[1][j] == b[2][j]:
                return (True, f"{b[0][j]} has won")

        if b[1][1] != " ":
            if b[0][0] == b[1][1] == b[2][2]:
                return (True, f"{b[1][1]} has won")
            if b[0][2] == b[1][1] == b[2][0]:
                return (True, f"{b[1][1]} has won")

        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    if self.turn == "X":
                        return (False, "X's turn")
                    return (False, "O's turn")

        return (True, "Cat's Game")


if __name__ == "__main__":
    board = Board()
    while True:
        print(board)
        over, status = board.whats_next()
        if over:
            print(status)
            break
        try:
            move_string = input(f"{status} Enter your move: ").strip()
            board.move(move_string)
        except TictactoeException as e:
            print(e.message)
