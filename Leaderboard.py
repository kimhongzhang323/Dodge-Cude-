import json

class SaveLoadSystem:

    def __init__(self, mainMenu):
        self.top5 = []

        self.num1 = 1
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0

        self.mainMenu1 = mainMenu
    @staticmethod
    def save_numbers_to_file(numbers, filename='saved_numbers5.json'):
        with open(filename, 'w') as file:
            json.dump(numbers, file)

    @staticmethod
    def load_numbers_from_file(filename='saved_numbers5.json'):
        try:
            with open(filename, 'r') as file:
                #This turns numbers into a list
                numbers = json.load(file)
            return numbers
        except FileNotFoundError:
            return []

    def save_and_display_top5(self, highscore):
        # Load numbers from the file
        numbers = self.load_numbers_from_file()

        # Get numbers from the user

        try:
            number = float(highscore)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Save numbers to the file
        self.save_numbers_to_file(numbers)

        # Display the top 5 highest numbers
        self.top5 = sorted(numbers, reverse=True)[:5]

    def mainMenuLog(self):
        self.num1 = self.top5[0]
        self.num2 = self.top5[1]
        self.num3 = self.top5[2]
        self.num4 = self.top5[3]
        self.num5 = self.top5[4]