"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox"."""
import random, sys

def get_birthdays(number_of_birthdays):
    """Returns a list of birthday dates."""
    birthdays = []
    for i in range(number_of_birthdays):
        day_of_year = random.randint(1, 365)
        if day_of_year > 334:
            month = 'Dec'
            day = day_of_year - 334
        elif day_of_year > 304:
            month = 'Nov'
            day = day_of_year - 304
        elif day_of_year > 273:
            month = 'Oct'
            day = day_of_year - 273
        elif day_of_year > 243:
            month = 'Sep'
            day = day_of_year - 243
        elif day_of_year > 212:
            month = 'Aug'
            day = day_of_year - 212
        elif day_of_year > 181:
            month = 'Jul'
            day = day_of_year - 181
        elif day_of_year > 151:
            month = 'Jun'
            day = day_of_year - 151
        elif day_of_year > 120:
            month = 'May'
            day = day_of_year - 120
        elif day_of_year > 90:
            month = 'Apr'
            day = day_of_year - 90
        elif day_of_year > 59:
            month = 'Mar'
            day = day_of_year - 59
        elif day_of_year > 31:
            month = 'Feb'
            day = day_of_year - 31
        elif day_of_year > 0:
            month = 'Jan'
            day = day_of_year - 0

        birthdays.append(month + str(day))
    return birthdays


def get_match(birthdays):
    """Returns the birthday that occurs more than once in the list."""

    # Compare each birthday to every other birthday:
    for a in range(0, len(birthdays)):
        for b in range(a + 1, len(birthdays)):  # if it was'nt a+1, it would compare the birthday with itself
                                                # and all birthdays would be printed.
            if birthdays[a] == birthdays[b]:
                return birthdays[a]  # Return the matching birthday.


# Display the intro:
print('Birthday Paradox (barebones version)')
print('by Al Sweigart al@inventwithpython.com')
print()
print('How many birthdays shall I generate? (Max 100)')
response = input('> ')
if not (0 < int(response) <= 100):
    print('That is larger than 100.')
    sys.exit()

num_bdays = int(response)

# Generate and display the birthdays:
print()
print('Here are', num_bdays, 'birthdays:')
birthdays = get_birthdays(num_bdays)
print(', '.join(birthdays))
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print('In this one simulation, ', end='')
if match != None:
    print('multiple people have a birthday on', match)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', num_bdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Running 100,000 simulations. Please wait...')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100000):
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        simMatch = simMatch + 1
print('Done.')

# Display simulation results:
probability = round(simMatch / 1000, 2)
print('Out of 100,000 simulations of', num_bdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', num_bdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That is probably more than you would think!')