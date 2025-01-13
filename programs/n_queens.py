#           <--- N Queens --->

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, num):
    #check the column
    for i in range(row):
        if (board[i][col] == 'O'):
            return False

    #check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == "O":
            return False

    #check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, num)):
        if board[i][j] == 'O':
            return False

    return True

def n_queen(board, row, num):
    if(row >= num):
        return True

    for col in range(num):
        if is_safe(board, row, col, num):
            board[row][col] = 'O' #place the queen
            if n_queen(board, row + 1, num):
                return True

            #Back Track if placing queen doesn't lead to a solution
            board[row][col] = 'X'
    return False


def main():
    print("      <--- Welcome To The N-Queens --->")
    num = int(input("Enter the size of the Board:"))
    board = [['X' for _ in range(num)] for _ in range(num)]

    if n_queen(board, 0, num):
        print_board(board)
    else:
        print("no solution possible ")

if __name__ == "__main__":
    main()