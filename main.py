import random
import MazeInput as MazeInput
import MazeSolver as MazeSolver


def main():
    maze_input = MazeInput.MazeInput()
    maze_solver = MazeSolver.MazeSolver(maze_input.prompt_the_user_for_seed(),
                                        maze_input.prompt_the_user_for_number_of_rows(),
                                        maze_input.prompt_the_user_for_number_of_columns())

    for counter in range(3):
        print(f"**Maze #{counter + 1}**")
        random.seed()
        maze_solver.draw_maze()
        maze_solver.print_maze()

        coins = 0
        starting_point = [0, 0]
        visited = [[0, 0]]
        path = []
        output = maze_solver.solve_maze(coins, starting_point, visited, path)

        if output:
            print("Congratulations! I found a solution for this maze as below: ")
            maze_solver.print_result(output[0], output[-1])
        else:
            print("Sorry, no solution can be found for this maze! ")
        print()


main()
