
state_capitals = [
    {'state': 'Alabama',
    'capital': 'Montgomery'},
    {'state': 'Alaska',
    'capital': 'Juneau'},
    {'state': 'Arizona',
    'capital': 'Phoenix'},
    {'state': 'Arkansas',
    'capital': 'Little Rock'},
    {'state': 'California',
    'capital': 'Sacramento'},
    {'state': 'Colorado',
    'capital': 'Denver'},
    {'state': 'Connecticut',
    'capital': 'Hartford'},
    {'state': 'Delaware',
    'capital': 'Dover'},
    {'state': 'Florida',
    'capital': 'Tallahassee'},
    {'state': 'Georgia',
    'capital': 'Atlanta'},
    {'state': 'Hawaii',
    'capital': 'Honolulu'},
    {'state': 'Idaho',
    'capital': 'Boise'},
    {'state': 'Illinios',
    'capital': 'Springfield'},
    {'state': 'Indiana',
    'capital': 'Indianapolis'},
    {'state': 'Iowa',
    'capital': 'Des Monies'},
    {'state': 'Kansas',
    'capital': 'Topeka'},
    {'state': 'Kentucky',
    'capital': 'Frankfort'},
    {'state': 'Louisiana',
    'capital': 'Baton Rouge'},
    {'state': 'Maine',
    'capital': 'Augusta'},
    {'state': 'Maryland',
    'capital': 'Annapolis'},
    {'state': 'Massachusetts',
    'capital': 'Boston'},
    {'state': 'Michigan',
    'capital': 'Lansing'},
    {'state': 'Minnesota',
    'capital': 'St. Paul'},
    {'state': 'Mississippi',
    'capital': 'Jackson'},
    {'state': 'Missouri',
    'capital': 'Jefferson City'},
    {'state': 'Montana',
    'capital': 'Helena'},
    {'state': 'Nebraska',
    'capital': 'Lincoln'},
    {'state': 'Neveda',
    'capital': 'Carson City'},
    {'state': 'New Hampshire',
    'capital': 'Concord'},
    {'state': 'New Jersey',
    'capital': 'Trenton'},
    {'state': 'New Mexico',
    'capital': 'Santa Fe'},
    {'state': 'New York',
    'capital': 'Albany'},
    {'state': 'North Carolina',
    'capital': 'Raleigh'},
    {'state': 'North Dakota',
    'capital': 'Bismarck'},
    {'state': 'Ohio',
    'capital': 'Columbus'},
    {'state': 'Oklahoma',
    'capital': 'Oklahoma City'},
    {'state': 'Oregon',
    'capital': 'Salem'},
    {'state': 'Pennsylvania',
    'capital': 'Harrisburg'},
    {'state': 'Rhoda Island',
    'capital': 'Providence'},
    {'state': 'South Carolina',
    'capital': 'Columbia'},
    {'state': 'South Dakoda',
    'capital': 'Pierre'},
    {'state': 'Tennessee',
    'capital': 'Nashville'},
    {'state': 'Texas',
    'capital': 'Austin'},
    {'state': 'Utah',
    'capital': 'Salt Lake City'},
    {'state': 'Vermont',
    'capital': 'Montpelier'},
    {'state': 'Virginia',
    'capital': 'Richmond'},
    {'state': 'Washington',
    'capital': 'Olympia'},
    {'state': 'West Virginia',
    'capital': 'Charleston'},
    {'state': 'Wisconsin',
    'capital': 'Madison'},
    {'state': 'Wyoming',
    'capital': 'Cheyenne'},
]

for i in state_capitals:
    i.update( {"correct": 0} )
    i.update( {"wrong": 0} )

import random

shuffled = random.sample(state_capitals, 50)
score = {'correct': 0, 'wrong': 0}

def game():
    for i in shuffled:
        temp = i["state"]
        answer = input(f'What is the Capital of {temp}').lower()
        if answer == (i["capital"]).lower():
            print(i["capital"])
            score['correct']+=1
            i['correct']+=1
            print(f"That was correct! You have answered total of {score['correct']} questions correctly this round! You have answered this question correctly {i['correct']} time(s)")
        elif answer == 'exit':
            break
        else:
            print(i["capital"])
            score['wrong']+=1
            i['wrong']+=1
            print(f"That was incorrect! You have got {score['wrong']} questions wrong so far this round. You have answered this question wrongly {i['wrong']} time(s)")


def gamestart(shuffled):
    print("Welcome challenger! Let's see how good you are at US geography!")
    game()
    choice = input("would you like to play again? Yes/No").lower()
    if choice == ("yes").lower():
        score['correct'] = 0
        score['wrong'] = 0
        shuffledagain = sorted(shuffled, key=lambda x: x['wrong'])
        shuffled = shuffledagain
        gamestart(shuffled)
    else:
        print("good bye")

gamestart(shuffled)
