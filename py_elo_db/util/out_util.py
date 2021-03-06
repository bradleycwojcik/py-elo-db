from typing import List

from py_elo_db.model.match import Match
from py_elo_db.model.player import Player


def print_help() -> None:
    """Print py-elo-db script usage."""
    print()
    print('py-elo-db -help:\n')
    print('- Record new match')
    print('\tmain.py -m "<home_name> <home_score>',
          '<away_score> <away_name> SD(optional)"')
    print('- Record new match file')
    print('\tmain.py -f <file_path>')
    print('- Print player stats')
    print('\tmain.py --stats')
    print('- Print player ratings')
    print('\tmain.py --ratings')
    print('- Print matches')
    print('\tmain.py --matches')
    print()


def print_no_file(path: str) -> None:
    """Print file does not exist message."""
    print('\tError - file does not exist:', path)


def print_stats(players: List[Player]) -> None:
    """Print player statistics."""
    player_list = sorted(players, key=lambda player:
                         round(player.wins / (player.wins + player.losses), 3),
                         reverse=True)

    print()
    print('Player, G, W, L, PCT, GF, GA')
    print('----------------------------')
    for player in player_list:
        games = player.wins + player.losses
        pct = round(player.wins / games, 3)
        print(str(player.name) + ', ' + str(games) + ', ' + str(player.wins) +
              ', ' + str(player.losses) + ', ' + str(pct) + ', ' +
              str(player.goals_for) + ', ' + str(player.goals_against))
    print()


def print_ratings(players: List[Player]) -> None:
    """Print player elo ratings."""
    player_list = sorted(players, key=lambda player: player.elo, reverse=True)

    print()
    print('Elo Ratings')
    print('-------------------------')
    for player in player_list:
        print(player.name + ' - ' + str(player.elo))

    print()


def print_matches(matches: List[Match]) -> None:
    """Print matches."""
    print()
    print('Matches')
    print('-------------------------')
    for match in matches:
        if match.sudden_death:
            print(match.home_player.name,
                  str(match.home_score) + ' - ' + str(match.away_score),
                  match.away_player.name, 'SD')
        else:
            print(match.home_player.name,
                  str(match.home_score) + ' - ' + str(match.away_score),
                  match.away_player.name)

    print()


def print_player_create(player: Player) -> None:
    """Print player created message."""
    print('...added new player,', player.name, player.elo)


def print_player_update(player: Player) -> None:
    """Print player updated message."""
    print('...updated player,', player.name, player.elo)


def print_player_retrieved(player: Player) -> None:
    """Print player retrieved message."""
    print('...retrieved player,', player.name, player.elo)


def print_recording_match() -> None:
    """Print recording new match message."""
    print('\nRecording new match...')


def print_match_recorded(match: Match) -> None:
    """Print match recorded message."""
    if (match.sudden_death):
        print('Matched Recorded,', match.home_player.name, match.home_score,
              match.away_score, match.away_player.name, 'SD')
    else:
        print('Matched Recorded,', match.home_player.name, match.home_score,
              match.away_score, match.away_player.name)
