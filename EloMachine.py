import pandas as pd # type: ignore

initial_elo = 1000
elo_ratings = {}
peak_elo_ratings = {}
k_factor = 40

def expected_score(elo_a, elo_b):
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))


def update_elo(winner_elo, loser_elo, k_factor):
    expected_win = expected_score(winner_elo, loser_elo)
    new_winner_elo = winner_elo + k_factor * (1 - expected_win)
    new_loser_elo = loser_elo + k_factor * (0 - (1 - expected_win))
    return round(new_winner_elo, 2), round(new_loser_elo, 2)



# Function to calculate Elo ratings for a match
def process_match(team_1, team_2, result, elo_ratings):
    """
    Process a match and update the Elo ratings for both teams.
    
    Args:
        team_1 (str): Name of the first team.
        team_2 (str): Name of the second team.
        result (str): Result of the match ('win', 'lose', or 'draw').
        elo_ratings (dict): Dictionary of current Elo ratings.
        peak_elo_ratings (dict): Dictionary of peak Elo ratings.

    Returns:
        dict: Updated Elo ratings.
    """
    # Initialize Elo ratings if teams are encountered for the first time
    if team_1 not in elo_ratings:
        elo_ratings[team_1] = initial_elo
    if team_2 not in elo_ratings:
        elo_ratings[team_2] = initial_elo

    # Get starting Elo ratings
    team_1_elo_start = elo_ratings[team_1]
    team_2_elo_start = elo_ratings[team_2]

    # Update Elo based on the result
    if result == 'win':  # Team 1 wins
        new_team_1_elo, new_team_2_elo = update_elo(team_1_elo_start, team_2_elo_start, k_factor)
    elif result == 'lose':  # Team 2 wins
        new_team_2_elo, new_team_1_elo = update_elo(team_2_elo_start, team_1_elo_start, k_factor)
    elif result == 'draw':  # Draw
        new_team_1_elo, new_team_2_elo = update_elo(team_1_elo_start, team_2_elo_start, k_factor / 2)
    else:
        raise ValueError("Invalid result. Use 'win', 'lose', or 'draw'.")

    # Update Elo ratings
    elo_ratings[team_1] = new_team_1_elo
    elo_ratings[team_2] = new_team_2_elo


    return elo_ratings


matches = [
    {"team_1": "Team A", "team_2": "Team B", "result": "win"},
    {"team_1": "Team C", "team_2": "Team D", "result": "lose"},
    {"team_1": "Team E", "team_2": "Team F", "result": "draw"},
    {"team_1": "Team A", "team_2": "Team C", "result": "win"},
    {"team_1": "Team B", "team_2": "Team D", "result": "lose"},
    {"team_1": "Team E", "team_2": "Team A", "result": "draw"},
]

# Process the matches
for match in matches:
    elo_ratings = process_match(
        match["team_1"], match["team_2"], match["result"], elo_ratings,
    )
    
    
    
all_teams_df = pd.DataFrame(sorted(elo_ratings.items(), key=lambda x: x[1], reverse=True), 
                            columns=["Team", "Elo Rating"])
print(all_teams_df)