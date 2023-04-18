import random


class MazeSolver:

    def __init__(self, seed, rows, columns):
        self.rows = rows
        self.columns = columns
        self.seed = seed
        self.maze = []

    def draw_maze(self):
        left_arrow_or_right_arrow = [" ←", " →"]
        up_arrow_or_down_arrow = [" ↑", " ↓"]
        self.maze = []
        for i in range(2 * self.rows - 1):
            self.maze.append([])
            for j in range(2 * self.columns - 1):
                self.maze[i].append(" ")

        print("Start drawing the maze...")

        for i in range(len(self.maze)):  # fill table

            if (i % 2) == 0:
                for j in range(len(self.maze[i])):

                    if (j % 2) == 1:
                        self.maze[i][j] = random.options(left_arrow_or_right_arrow, weights=[2, 3])[0]

                    else:
                        num = str(random.randint(1, 99))

                        if len(str(num)) < 2:
                            num = " " + num
                        self.maze[i][j] = num

            else:
                for j in range(len(self.maze[i])):

                    if (j % 2) == 1:
                        self.maze[i][j] = " "

                    else:
                        self.maze[i][j] = random.options(up_arrow_or_down_arrow, weights=[2, 3])[0]

        self.maze[0][0] = " S"
        self.maze[2 * self.rows - 2][2 * self.columns - 2] = " D"

    def print_maze(self):
        print("The maze is as below: ")
        for row in self.maze:
            print(*row, sep=" ")
        print()

    def get_neighbours(self, v):

        neighbours = []
        row = v[0]
        col = v[1]

        if col / 2 < self.columns - 1 and self.maze[row][col + 1] == " →":
            neighbours.append([row, col + 2])

        if row / 2 < self.rows - 1 and self.maze[row + 1][col] == " ↓":
            neighbours.append([row + 2, col])

        if col / 2 > 1 and self.maze[row][col - 1] == " ←":
            neighbours.append([row, col - 2])

        if row / 2 > 1 and self.maze[row - 1][col] == " ↑":
            neighbours.append([row - 2, col])

        return neighbours

    def solve_maze(self, coins, place, visited, path):

        path.append(place)

        if self.maze[place[0]][place[1]] == " D":
            return coins, place, visited, path

        if self.maze[place[0]][place[1]] != " S":
            coins += int(self.maze[place[0]][place[1]])

        places_to_go = self.get_neighbours(place)

        go_to_places = []
        for neighbour in places_to_go:

            if neighbour not in visited:
                go_to_places.append(neighbour)
                visited.append(neighbour)

        for neighbour in go_to_places:
            found = self.solve_maze(coins, neighbour, visited, path)

            if found:
                return found

        path.pop()
        return False

    def print_result(self, coins, path):
        for point in path:
            self.maze[point[0]][point[1]] = " +"
        self.maze[0][0] = " S"
        self.maze[2 * self.rows - 2][2 * self.columns - 2] = " D"
        for row in self.maze:
            print(*row, sep=" ")
        print()
        print(f'The amount of coins collected: {coins}')
