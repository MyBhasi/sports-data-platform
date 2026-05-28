from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_fixtures(df: DataFrame) -> DataFrame:
    return (
        df.dropDuplicates(["fixture_id"])
        .withColumn("match_date", F.to_date("match_date"))
        .withColumn("ingested_at", F.current_timestamp())
        .filter(F.col("fixture_id").isNotNull())
    )


def clean_players(df: DataFrame) -> DataFrame:
    return (
        df.dropDuplicates(["player_id"])
        .withColumn("ingested_at", F.current_timestamp())
        .filter(F.col("player_id").isNotNull())
    )
