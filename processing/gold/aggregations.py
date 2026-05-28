from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def top_scorers(df: DataFrame, top_n: int = 10) -> DataFrame:
    return (
        df.groupBy("player_id", "player_name", "team_name")
        .agg(F.sum("goals").alias("total_goals"))
        .orderBy(F.desc("total_goals"))
        .limit(top_n)
    )


def team_standings(df: DataFrame) -> DataFrame:
    return (
        df.groupBy("team_id", "team_name")
        .agg(
            F.sum("wins").alias("total_wins"),
            F.sum("draws").alias("total_draws"),
            F.sum("losses").alias("total_losses"),
            F.sum("goals_for").alias("total_goals_for"),
            F.sum("goals_against").alias("total_goals_against"),
        )
        .withColumn("points", F.col("total_wins") * 3 + F.col("total_draws"))
        .orderBy(F.desc("points"))
    )
