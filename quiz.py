import random
from Question import Question
import time


def science():
    print("__________*****Great you have selected Science, lets begin*****__________\n ")


question_prompts = [
    "What is a shaddock?\n (a) A fish, the offspring of a male shad and a female haddock \n(b) A crystal, such as quartz, that sticks out from a mineral vein \n(c) A plant that is a member of the nightshade family \n(d) A grapefruit\n",
    "Which one of the following instruments is used to measure humidity?\n (a) Anemometer \n(b) Ammeter \n(c) Hygrometer \n(d) Barometer\n",
    "Which two planets are most similar in size diameter wise?\n (a) Mars and Mercury \n(b) Venus and Earth \n(c) Uranus and Neptune \n(d) Jupiter and Saturn\n",
    "If a hertz is equal to one cylce per second, how manyh cycles per second does a megahertz  equal?\n (a) 1/1,000 \n(b) 1,000 \n(c) 1,000,000\n(d) 1,000,000,000\n",
    "Which color is not considered to be one of the primary colors of light?\n(a) Red \n(b) Yellow \n(c) Green \n(d) Blue\n",
    "What causes the disease toxoplasmosis?\n (a) A bacterium \n(b) A protozoan \n(c) A virus \n(d) A prion\n",
    "What is the slowest wind speed a hurricane can have according to the Saffir-Simpson scale?\n(a) 50 m.p.h \n(b) 74 m.p.h \n(c) 96 m.p.h \n(d) 110 m.p.h\n",
    "Which of the following heavenly bodies have never had a spacecraft landed on it?\n(a) Venus \n(b) Mars \n(c) The moon \n(d) Jupiter\n",
    "Meat should be kept frozen at what temperature in degrees Fahrenheit?\n(a) 0 degrees or below \n(b) Between 10 and 20 degrees \n(c) Between 20 and 30 degrees \n(d) Just below 32 degrees\n",
    "Many scientists think that some of the dinosaurs did not go extinct, but rather evolved into what kind of creature?\n(a) Amphibians \n(b) Reptiles \n(c) Birds \n(d) Mammals\n",
    "In 1989, scientists from Norway discovered that there are far more viruses in oceans, lakes, and streams than previously believed.  How many viruses did they find that a milliliter of natural water might contain?\n(a) up to 250 \n(b) up to 25,000 \n(c) up to 2,500,000 \n(d) up to 250,000,000\n",
    "In which kind of geometry is the sum of the angles inside a triangle exactly equal to 180 degrees?\n(a) elliptical \n(b) Euclidean \n(c) hyperbolic \n(d) linear\n",
    "What is the name of the disease that has been referred to as the DISEASE OF KINGS?\n(a) hemophilia \n(b) jaundice \n(c) rubella \n(d) syphilis\n",
    "What disease causes a buildup of fluid pressure in the eyeball and damages the optic nerve at the back of the eye?\n(a) astigmatism \n(b) cataract \n(c) glaucoma \n(d) retinitis\n",
    "What would be the most likely thing one would do with the compound MgSO4 7H2O?\n(a) power a car \n(b) blow up a building \n(c) soak ones feet \n(d) fertilize a lawn\n",
    "Amps are a unit of measurement of what?\n(a) electric charge \n(b) electric current \n(c) electric field strength \n(d) electric potential\n",
    "In which century was the greatest number of chemical elements discovered?\n(a)  17th \n(b) 18th \n(c)  19th \n(d) 20th\n",
    "Louis Pasteur developed which vaccine?\n(a) polio \n(b) rabies \n(c) smallpox \n(d) anthrax\n",
    "How long ago did dinosaurs become extinct?\n(a) 10,000 years \n(b) 600,000 years \n(c) 6 million years \n(d) 60 million years\n",
    "Which of the following food items have the least calories?\n(a) 5 ounces of whole milk \n(b) 5 ounces of beer \n(c) 5 teaspoons of sugar \n(d) 5 ounces of vegetable oil\n",
    "The scapula is more commonly called the what? \n(a) shoulder blade \n(b) knee cap \n(c) femur \n(d) lower jaw bone\n",
    "Which of the following are true during a lunar eclipse? \n(a) The sun is between the earth and the moon \n(b) the earth is between the sun and the moon \n(c) the sun is between the earth and the moon \n(d) none of the above\n",
    "What kinds of quarks form the protons and neutrons in the atoms of matter?\n(a)  strange and charmed \n(b) top and bottom \n(c) up and down \n(d) all of the above\n",
    "What country became the third one to launch a spacecraft to the moon in January 1990?\n(a) China \n(b) France \n(c) Japan \n(d) United Kingdom\n",
]

random.shuffle(question_prompts)

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "a"),
    Question(question_prompts[12], "a"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "a"),
    Question(question_prompts[16], "a"),
    Question(question_prompts[17], "a"),
    Question(question_prompts[18], "a"),
    Question(question_prompts[19], "a"),
    Question(question_prompts[20], "a"),
    Question(question_prompts[21], "a"),
    Question(question_prompts[22], "a"),
    Question(question_prompts[23], "a"),

]


def run_quiz(questions):
    score = 0
    count = 0
    for question in questions:
        count = count + 1
        answer = input(question.prompt)
        print()

        if answer == question.answer:
            score += 1
        if count > 9:
            break

    if score >= 8:
        print("Quiz passed you got ", score, " out of 10 questions correct")
        return

    else:
        print("Quiz failed you got ", score, " out of 10 questions correct")
        return


def mathematics():
    print("__________*****Great you have selected Mathematics, lets begin*****__________\n ")
    player_points = 0

    for a in range(0, 10):
        a = random.randint(2, 5)
        b = random.randint(2, 5)

        print("What is " + str(a) + " times " + str(b) + "?")

        answer = int(input("What is your answer? "))

        if answer == (a * b):
            print("Correct!")
            print()
            player_points += 1

        else:
            print("Incorrect. The answer is " + str(a * b))
            player_points -= 2

    if player_points < 0:
        player_points = 0

        print("Player has " + str(player_points))

    if player_points == 10:
        print("Quiz Passed. Thank you for playing!")
    exit(0)


name = str(input("Enter your name: "))

print("\n")


def mainmenu():
    print("welcome to the quiz " + str(name))
    print()
    print("1. For Science")
    print("2. For Mathematics")
    selection = int(input("Enter choice: "))
    print()
    if selection == 1:
        science()
    elif selection == 2:
        mathematics()
    else:
        print("Invalid choice. Choose from 1-2")


mainmenu()

run_quiz(questions)



