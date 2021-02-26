class CheckersBoard:

    def __init__(self, board):
        self.B = board
        self.N = len(board)
        self.score = 0
        self.starting_position = self.find_Jafar()

    def jafars_best_result(self):
        self.score = self.all_possible_kills_of_position(self.starting_position)

    def all_possible_kills_of_position(self, position):
        r, c = position
        if r < 2:
            return 0
        upper_right = (r - 1, c + 1)
        next_right = (r - 2, c + 2)
        upper_left = (r - 1, c - 1)
        next_left = (r - 2, c - 2)
        upper_right_possible_kills = 0
        upper_left_possible_kills = 0
        if (
                self.check_if_on_board([next_right, upper_right])
                and self.check_if_occupied(upper_right)
                and not self.check_if_occupied(next_right)
        ):
            upper_right_possible_kills += 1
            upper_right_possible_kills += self.all_possible_kills_of_position(next_right)
        if (self.check_if_on_board([next_left, upper_left])
                and self.check_if_occupied(upper_left)
                and not self.check_if_occupied(next_left)
        ):
            upper_left_possible_kills += 1
            upper_left_possible_kills += self.all_possible_kills_of_position(next_left)
        score = max(upper_left_possible_kills, upper_right_possible_kills)
        return score

    def check_if_on_board(self, positions):
        for r, c in positions:
            is_on_board = r in range(0, self.N) and c in range(0, self.N)
            if not is_on_board:
                return False
            return True

    def check_if_occupied(self, position):
        r, c = position
        if self.B[r][c] == 'X':
            return True
        return False

    def find_Jafar(self):
        r = 0
        while r < self.N:
            if 'O' in self.B[r]:
                return r, self.B[r].index('O')
            r += 1


if __name__ == '__main__':
    B = ['.'] * 6
    B[0] = "..X..."
    B[1] = "......"
    B[2] = "....X."
    B[3] = ".X...."
    B[4] = "..X.X."
    B[5] = "...O.."
    c = CheckersBoard(B)
    c.jafars_best_result()
    print(c.score)
