def score(dices, category):
    if category == "Yahtzee":
        if len(set(dices)) == 1:
            return 50
        else:
            return 0
    return sum(dices)