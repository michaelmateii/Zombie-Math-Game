import random
import math

# Frågar användaren om ett heltal inom ett visst intervall
def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Vänligen ange ett heltal mellan {min_val} och {max_val}.")
        except ValueError:
            print("Felaktig inmatning. Ange ett heltal.")

# Frågar efter en sträng och kontrollerar att det är ett av de godkända alternativen
def get_valid_str(prompt, valid_options):
    while True:
        value = input(prompt).lower()
        if value in valid_options:
            return value
        print(f"Ogiltigt val. Välj mellan: {', '.join(valid_options)}")

# Genererar en mattefråga som inte har använts för många gånger
def generate_question(value, used_questions, max_occurrences):
    while True:
        a = random.randint(0, 12)
        
        # Multiplikation, division och modulo använder samma struktur
        question = (a, value)
        count = used_questions.get(question, 0)
        
        # Kolla om frågan använts för få gånger
        if count < max_occurrences:
            used_questions[question] = count + 1
            return question

# Räknar ut rätt svar beroende på valt räknesätt
def calculate_answer(operator, a, b):
    if operator == "*":
        return a * b
    elif operator == "//":
        return a // b
    elif operator == "%":
        return a % b

# Ställer mattefrågan och kollar om spelaren svarar rätt
def ask_math_question(operator, a, b):
    user_answer = get_valid_int(f"Vad blir {a} {operator} {b}? ", -100, 200)
    return user_answer == calculate_answer(operator, a, b)

# Låter användaren välja en dörr, en av dem innehåller zombies
def choose_door(num_doors):
    zombie_door = random.randint(1, num_doors)
    choice = get_valid_int(f"Välj en dörr (1 - {num_doors}): ", 1, num_doors)
    if choice == zombie_door:
        print(f"Du valde dörr {choice}. Tyvärr! Zombiesarna fanns där!")
        return False
    else:
        print(f"Puh! Du valde rätt dörr. Zombiesarna gömde sig bakom dörr {zombie_door}.")
        return True

# Huvudprogrammet som kör spelet
def run_game():
    settings = {}
    first_run = True
    keep_playing = True
    previous_result = None  # 'win' eller 'lose'

    while keep_playing:
        # Om det är första gången eller man vann förra gången ska nya inställningar väljas
        if first_run or previous_result == "win":
            num_questions = get_valid_int("Hur många frågor? (12-39): ", 12, 39)
            operator = get_valid_str("Välj räknesätt (*, //, %): ", ["*", "//", "%"])

            if operator == "*":
                value = get_valid_int("Välj en tabell (2-12): ", 2, 12)
            else:
                value = get_valid_int("Välj en divisor (2-5): ", 2, 5)

            settings = {
                "num_questions": num_questions,
                "operator": operator,
                "value": value
            }

        used_questions = {}
        max_occurrences = math.ceil(settings["num_questions"] / 13)
        success = True

        # Frågeloopen
        for question_num in range(1, settings["num_questions"] + 1):
            print(f"\nFråga {question_num} av {settings['num_questions']}")
            a, b = generate_question(settings["value"], used_questions, max_occurrences)

            if not ask_math_question(settings["operator"], a, b):
                print("Fel svar! Du förlorade.")
                success = False
                break

            if question_num != settings["num_questions"]:
                remaining_doors = settings["num_questions"] - question_num + 1
                if not choose_door(remaining_doors):
                    print("Zombiesarna tog dig! Spelet över.")
                    success = False
                    break

        if success:
            print("Grattis! Du svarade rätt på alla frågor och undvek zombiesarna!")
            previous_result = "win"
        else:
            previous_result = "lose"

        # Frågar om spelaren vill fortsätta
        play_again = get_valid_str("Vill du spela igen? (ja/nej): ", ["ja", "j", "nej", "n"])
        if play_again in ["nej", "n"]:
            keep_playing = False
        else:
            first_run = False  # Fortsätt utan att fråga om inställningar igen om man förlorat

# Startar spelet
if __name__ == "__main__":
    run_game()