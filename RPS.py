import random
def play():
    user=input("'r'for rock , 'p' for paper , 's' for scissors\n")
    computer=random.choice(['r','s','p'])

    if user==computer:
        return 'It\'s a tie'
    if is_win(computer,user):
        return 'You won !'
    return 'You lost'

    


def is_win(computer,user):
    if(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        return True
print(play())