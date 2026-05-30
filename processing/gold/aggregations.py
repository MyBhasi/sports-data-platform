from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def top_scorers(df: DataFrame, top_n: int = 10) -> DataFrame:
    return (
        df.groupBy("player_id", "player_name", "team_name", "competition_name")
        .agg(
            F.coalesce(F.sum("goals"), F.lit(0)).alias("total_goals"),
            F.coalesce(F.sum("assists"), F.lit(0)).alias("total_assists"),
            F.coalesce(F.sum("penalties"), F.lit(0)).alias("total_penalties"),
        )
        .orderBy(F.desc("total_goals"))
        .limit(top_n)
        .withColumn("updated_at", F.current_timestamp())
    )


def team_standings(df: DataFrame) -> DataFrame:
    return (
        df.groupBy("team_id", "team_name", "competition_name")
        .agg(
            F.sum("won").alias("total_wins"),
            F.sum("draw").alias("total_draws"),
            F.sum("lost").alias("total_losses"),
            F.sum("goals_for").alias("total_goals_for"),
            F.sum("goals_against").alias("total_goals_against"),
            F.sum("points").alias("total_points"),
        )
        .orderBy(F.desc("total_points"))
        .withColumn("updated_at", F.current_timestamp())
    )


def match_results(df: DataFrame) -> DataFrame:
    return (
        df.filter(F.col("status") == "FINISHED")
        .select(
            "match_id",
            "competition_name",
            "matchday",
            "match_date",
            "home_team_name",
            "away_team_name",
            "full_time_home",
            "full_time_away",
            "winner",
            "referee_name",
        )
        .withColumn("updated_at", F.current_timestamp())
    )


def referee_stats(df: DataFrame) -> DataFrame:
    return (
        df.filter(F.col("status") == "FINISHED")
        .filter(F.col("referee_name").isNotNull())
        .groupBy("referee_name", "referee_nationality")
        .agg(F.count("match_id").alias("matches_officiated"))
        .orderBy(F.desc("matches_officiated"))
        .withColumn("updated_at", F.current_timestamp())
    )
