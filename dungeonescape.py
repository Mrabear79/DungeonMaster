from random import randint
import time


def main():
    word = "a"
    sword = 5
    intro()
    while True:
        sword, word, finished = TakeTurn(word, sword)
        if finished:
            break
        if sword == 1:
            word1 = "sword"
        else:
            word1 = "swords"
        print("You have", sword, word1)
    if sword < 1:
        print("Out of swords! Sorry you lose!")
    else:
        print("You Win!!!")


def intro():
    time = [1, 2.5, 2, 1.5, 1, 2, 1]
    text = ["Your in a maze, and you are lost",
            "Im sure there\'s evil lurking in the shadows...",
            "There\'s five swords to make it out alive.", "Be wise with them!",
            "Ready to go!"]
    print_on_a_timer(time, text)


def TakeTurn(word1, sword1):
    time.sleep(1.5)
    if sword1 < 1:
        return sword1, word1, True
    print("The path T\'s,\nShould we go left (L), right (R) or straight (S)?")
    turning = str(input().lower())
    word1 = "another"
    while turning not in ["l", "r", "s"]:
        time.sleep(0.7)
        print("I didn\'t understand that")
        turning = input().lower()
    choice = randint(1, 10)
    time.sleep(1)
    if choice == 1:
        print("You found the exit!")
        return sword1, word1, True
    elif choice == 2:
        print("You found a sword!")
        time.sleep(1)
        sword1 = sword1 + 1
        return sword1, word1, False
    elif choice == 3:
        print("You found two swords!")
        time.sleep(1)
        sword1 = sword1 + 2
        return sword1, word1, False
    elif choice == 4:
        print("You found three swords!")
        time.sleep(1)
        sword1 = sword1 + 3
        return sword1, word1, False
    elif choice == 5:
        print("A demon atacks you!")
        time.sleep(2)
        print("You lost two swords")
        time.sleep(1)
        sword1 = sword1 - 2
        return sword1, word1, False
    elif choice == 6:
        print("You found a small treasurechest!")
        time.sleep(1.5)
        print("You found a sword!")
        time.sleep(1)
        sword1 = sword1 + 1
        return sword1, word1, False
    elif choice == 7:
        print("A witch confuses you with a spell!")
        time.sleep(2)
        print("You lost a sword")
        time.sleep(1)
        sword1 = sword1 - 1
        return sword1, word1, False
    elif choice == 8:
        print("A warlock casts a spell on you!")
        time.sleep(2.5)
        print("You feel panic and fear consuming you...")
        time.sleep(1.5)
        print("You cannot fight dark magic like this!")
        time.sleep(1)
        print("You lost three swords")
        time.sleep(1)
        sword1 = sword1 - 3
        return sword1, word1, False
    elif choice == 9:
        print("You encounter a woman unconscious on the floor...")
        time.sleep(1.5)
        print("As your helping her she turns into a vampire and attacks you")
        time.sleep(2)
        print("You lost two swords")
        time.sleep(1)
        sword1 = sword1 - 2
        return sword1, word1, False
    else:
        print("A zombie springs from the shadows onto you!")
        time.sleep(2)
        print("You barely get escape with your life...")
        time.sleep(1.5)
        print("Or did you? You notice you lost five swords escaping...")
        time.sleep(1)
        sword1 = sword1 - 5
        return sword1, word1, False


def goblin(sword):
    time1 = [1, 2.5, 1, 1, 1]
    text = ["'Want to play a game?\n There is three possible outcomes:'",
            "You lose a sword", "You get a sword", "Nothing happens"]
    print_on_a_timer(time1, text)
    goblin = 0
    while goblin == 0:
        print("Will you play? Y or N?")
        choice2 = input().lower()
        time.sleep(1)
    if choice2 not in ["y", "n"]:
        print("Sorry I don\'t understand that")
    elif choice2 not in ["y"]:
        print("Goodbye")
        TakeTurn()
    else:
        print("Ready to play!")
        time.sleep(1)
        print("Shaking...")
        time.sleep(1)
        print("Throwing...")
        time.sleep(1)
        print("Rolling...")
        time.sleep(1)
        roulette = randint(1, 3)
        if roulette == 1:
            print("Nothing happens")
            goblin = 1
        elif roulette == 2:
            print("The goblin laughs and takes one of your swords...")
            sword = sword - 1
            goblin = 1
        else:
            print("He screams with anger and tosses you a sword!")
        sword = sword + 1
        goblin = 1

    def treasurechest(sword):
        treasure = 1
        while treasure == 1:
            print("You found a treasure chest! Will you open it? Y or N?")
            chest = input().lower()
            if chest not in ["y", "n"]:
                print("Sorry, I don\'t understand that")
            elif chest not in ["y"]:
                print("Goodbye")
                treasure = 0
            else:
                time.sleep(1)
                print("You break the lock...")
                time.sleep(1)
                print("You grip the chest...")
                time.sleep(1)
                print("Opening...")
                time.sleep(1)
                chest = randint(1, 6)
                if chest == 1:
                    print("You found a sword!")
                    sword = sword + 1
                    treasure = 0
                elif chest == 2:
                    print("You found two swords!")
                    sword = sword + 2
                    treasure = 0
                elif chest == 3:
                    print("A ghostly hand reaches out and steals one of your swords!")
                    shield = shield - 1
                    treasure = 0
                elif chest == 4:
                    print("Everything goes black, you wake and two of your swords are gone!")
                    shield = shield - 2
                    treasure = 0
                elif chest == 5:
                    print("The chest is empty")
                    treausre = 0
                else:
                    print("A goblin in the chest says...")
                    time.sleep(2)
                    goblin()


def print_on_a_timer(times, lines):
    for times, lines in zip(times, lines):
        time.sleep(times)
        print(lines)


main()
