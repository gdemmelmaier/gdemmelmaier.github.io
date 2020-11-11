import json
with open('test.json') as jsonfile:
    data = json.load(jsonfile)
    phase = data['Phase']
    turn = data['Turn']
    turn += 1
    board = list(data['Board'].values())
    player = data['Player']
    difficulty = data['Difficulty']
    filename = 'test.json'
    jsonfile.close()
print(board)