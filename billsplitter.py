from random import choice

def input_n(num):
    try:
        num = int(num)
        assert num > 0
        return num
    except (ValueError, AssertionError):
        return False


def main():
    n = input_n(input("Enter the number of friends joining (including you):\n"))
    if n:
        print("Enter the name of every friend (including you), each on a new line:")
        party = {input("> "): 0 for _ in range(n)}
        total_bill = int(input("Enter the total bill value:\n").strip())
        party = {key: round(total_bill / n, 2) for key in party.keys()}
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if answer == "Yes":
            lucky = choice(list(party.keys()))
            print(f"{lucky} is the lucky one!")
            for key in party.keys():
                if key != lucky:
                    party[key] = round(total_bill / (n - 1), 2)
                else:
                    party[key] = 0
        elif answer == "No":
            print("No one is going to be lucky")
        print(party)
    else:
        print("No one is joining for the party")


if __name__ == '__main__':
    main()
