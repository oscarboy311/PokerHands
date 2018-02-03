from GameCard import GameCard

def main():
    number1, type1 = input("Enter your first card (NUMBER and TYPE): ").split()
    number2, type2 = input("Enter your second card (NUMBER and TYPE): ").split()

    card1 = GameCard(int(number1), type1)
    card2 = GameCard(int(number2), type2)
    print(str(card1.number) +" "+ card1.type)
    print(str(card2.number) +" "+ card2.type)

    


if __name__ == "__main__":
    main()