
class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of both Batsman and Bowler classes and call the play() method for each object based on user input.
if __name__ == "__main__":
    while True:
        print("Choose a player type:")
        print("1. Batsman")
        print("2. Bowler")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            batsman = Batsman()
            batsman.play()  # This will print "The batsman is batting."
        elif choice == "2":
            bowler = Bowler()
            bowler.play()   # This will print "The bowler is bowling."
        elif choice == "3":
            print("Thank you for using the player simulation.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
