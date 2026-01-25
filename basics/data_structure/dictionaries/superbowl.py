# List of dictionaries for Super Bowl

Kansas_City_Chiefs = [
    {
        'name': 'Patrick Mahomes',
        'position': 'Quarterback',
        'jersey_number': 1,
        'game_statistics': {
            'passing_yards': 200,
            'touchdowns': 3,
            'interceptions': 1
        }
    },
    {
        'name': 'Isiah Pacheco',
        'position': 'Running Back',
        'jersey_number': 2,
        'game_statistics': {
            'passing_yards': 100,
            'touchdowns': 2,
            'fumbles': 1
        }
    },
    {
        'name': 'Jalen Milroe',
        'position': 'Quarterback',
        'jersey_number': 1,
        'game_statistics': {
            'passing_yards': 200,
            'touchdowns': 3,
            'interceptions': 1
        }
    },
    {
        'name': 'Tyreek Hill',
        'position': 'Receiver',
        'jersey_number': 1,
        'game_statistics': {
            'passing_yards': 200,
            'touchdowns': 3,
            'interceptions': 1
        }
    },
    {
        'name': 'Travis Kelce',
        'position': 'Tight End',
        'jersey_number': 1,
        'game_statistics': {
            'passing_yards': 200,
            'touchdowns': 3,
            'interceptions': 1
        }
    }
]

print(Kansas_City_Chiefs)
Kansas_City_Chiefs[0]['game_statistics']['passing_yards'] = 200
print(Kansas_City_Chiefs)

# Print out all list of player positions
for player in Kansas_City_Chiefs:
    print(f"Player: {player['name']}, Position: {player['position']}")

# Calculate the average statistic of all player
avg_passing_yards = sum(player['game_statistics'].get('passing_yards', 0) for player in Kansas_City_Chiefs) / len(Kansas_City_Chiefs)
print(f"Average Passing Yards: {avg_passing_yards}")
avg_touchdowns = sum(player['game_statistics'].get('touchdowns', 0) for player in Kansas_City_Chiefs) / len(Kansas_City_Chiefs)
print(f"Average Touchdowns: {avg_touchdowns}")
avg_interceptions = sum(player['game_statistics'].get('interceptions', 0) for player in Kansas_City_Chiefs) / len(Kansas_City_Chiefs)
print(f"Average Interceptions: {avg_interceptions}")

