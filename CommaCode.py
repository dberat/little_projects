spam = ['apples', 'bananas', 'tofu', 'cats',"cow","snake","dog"]

def comma(liste):
    if not liste:
        return " "
    else:
        for i in liste[:-1]:
            print(i,end=", ")
        print(f"and {liste[-1]}" )

bacon = []
comma(bacon)
comma(spam)
