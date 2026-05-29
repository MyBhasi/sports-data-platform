from ingestion.loaders.silver_loader import SilverLoader
from processing.silver.transformations import (
    flatten_fixtures,
    flatten_scorers,
    flatten_squad,
    flatten_standings,
)


def main():
    loader = SilverLoader()
    spark = loader.spark

    try:
        print("Silver layer processing started...")

        print("\n[1/4] Fixtures")
        fixtures_df = flatten_fixtures(spark, loader.bronze_path("fixtures"))
        loader.write(fixtures_df, "fixtures")
        fixtures_df.show(5, truncate=False)

        print("\n[2/4] Scorers")
        scorers_df = flatten_scorers(spark, loader.bronze_path("scorers"))
        loader.write(scorers_df, "scorers")
        scorers_df.show(5, truncate=False)

        print("\n[3/4] Standings")
        standings_df = flatten_standings(spark, loader.bronze_path("standings"))
        loader.write(standings_df, "standings")
        standings_df.show(5, truncate=False)

        print("\n[4/4] Squad (players per team)")
        squad_df = flatten_squad(spark, "data/bronze/players/*/*.json")
        loader.write(squad_df, "squad")
        squad_df.show(5, truncate=False)

        print("\nDone. Silver layer loaded.")

    finally:
        loader.stop()


if __name__ == "__main__":
    main()