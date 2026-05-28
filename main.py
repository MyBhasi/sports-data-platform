import time

from ingestion.api.football_api import FootballAPIClient
from ingestion.loaders.bronze_loader import BronzeLoader


def main():
    client = FootballAPIClient()
    loader = BronzeLoader()

    print("Fetching fixtures...")
    fixtures = client.get_fixtures(league_id=2021, season=2024)
    path = loader.save(fixtures, "fixtures")
    print(f"Saved fixtures → {path}")

    print("Fetching standings...")
    standings = client.get_standings(league_id=2021, season=2024)
    path = loader.save(standings, "standings")
    print(f"Saved standings → {path}")

    print("Fetching teams...")
    teams = client.get_teams(league_id=2021, season=2024)
    path = loader.save(teams, "teams")
    print(f"Saved teams → {path}")

    print("Fetching players for all teams...")
    for team in teams["teams"]:
        team_id = team["id"]
        team_name = team["name"]
        print(f"  Fetching players → {team_name} (id={team_id})")
        try:
            players = client.get_players(team_id=team_id, season=2024)
            loader.save(players, f"players/{team_id}")
        except Exception as e:
            print(f"  Skipping {team_name} (id={team_id}): {e}")
        time.sleep(7)  # free tier allows 10 calls/min → wait 7s between calls

    print("Fetching goal scorers...")
    scorers = client.get_scorers(league_id=2021, season=2024)
    path = loader.save(scorers, "scorers")
    print(f"Saved scorers → {path}")

    print("Done. Bronze layer loaded.")


if __name__ == "__main__":
    main()

