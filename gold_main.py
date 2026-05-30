from dotenv import load_dotenv

load_dotenv()

from ingestion.loaders.gold_loader import GoldLoader
from processing.gold.aggregations import (
    match_results,
    referee_stats,
    team_standings,
    top_scorers,
)


def main():
    loader = GoldLoader()

    try:
        print("Gold layer processing started...")

        print("\n[1/4] Top Scorers")
        scorers_df = loader.silver("scorers")
        loader.write(top_scorers(scorers_df), "top_scorers")

        print("\n[2/4] Team Standings")
        standings_df = loader.silver("standings")
        loader.write(team_standings(standings_df), "team_standings")

        print("\n[3/4] Match Results")
        fixtures_df = loader.silver("fixtures")
        loader.write(match_results(fixtures_df), "match_results")

        print("\n[4/4] Referee Stats")
        loader.write(referee_stats(fixtures_df), "referee_stats")

        print("\nDone. Gold layer loaded.")

    finally:
        loader.stop()


if __name__ == "__main__":
    main()
