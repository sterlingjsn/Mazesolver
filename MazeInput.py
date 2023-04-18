class MazeInput:

    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.seed = 0

    def prompt_the_user_for_seed(self):
        while True:
            try:
                self.seed = int(input("Enter seed for maze generation: "))
            except ValueError:
                print("Input must be an integer")
            else:
                return self.seed

    def prompt_the_user_for_number_of_rows(self):
        while True:
            try:
                self.rows = int(input("Enter number of rows in range [5, 10]: "))
            except ValueError:
                print("Input must be an integer!")
            else:
                if self.rows > 10 or self.rows < 5:
                    print("Invalid input!")
                else:
                    return self.rows

    def prompt_the_user_for_number_of_columns(self):
        while True:
            try:
                self.columns = int(input("Enter number of columns in range [5, 10]: "))
            except ValueError:
                print("Input must be an integer!")
            else:
                if self.columns > 10 or self.columns < 5:
                    print("Invalid input!")
                if self.columns == self.rows:
                    print("This must be different from number of rows!")
                else:
                    print()
                    return self.columns

    def get_seed(self):
        return self.seed
