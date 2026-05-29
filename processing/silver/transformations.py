from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F


def flatten_fixtures(spark: SparkSession, bronze_path: str) -> DataFrame:
    df = spark.read.option("multiline", "true").json(bronze_path)
    df = df.select(
        F.col("competition.id").alias("competition_id"),
        F.col("competition.name").alias("competition_name"),
        F.col("competition.code").alias("competition_code"),
        F.explode("matches").alias("match"),
    )
    return (
        df.select(
            F.col("competition_id"),
            F.col("competition_name"),
            F.col("competition_code"),
            F.col("match.id").alias("match_id"),
            F.col("match.utcDate").alias("utc_date"),
            F.col("match.status").alias("status"),
            F.col("match.matchday").alias("matchday"),
            F.col("match.stage").alias("stage"),
            F.col("match.homeTeam.id").alias("home_team_id"),
            F.col("match.homeTeam.name").alias("home_team_name"),
            F.col("match.homeTeam.shortName").alias("home_team_short_name"),
            F.col("match.awayTeam.id").alias("away_team_id"),
            F.col("match.awayTeam.name").alias("away_team_name"),
            F.col("match.awayTeam.shortName").alias("away_team_short_name"),
            F.col("match.score.winner").alias("winner"),
            F.col("match.score.fullTime.home").alias("full_time_home"),
            F.col("match.score.fullTime.away").alias("full_time_away"),
            F.col("match.score.halfTime.home").alias("half_time_home"),
            F.col("match.score.halfTime.away").alias("half_time_away"),
        )
        .withColumn("match_date", F.to_date("utc_date"))
        .withColumn("ingested_at", F.current_timestamp())
        .filter(F.col("match_id").isNotNull())
        .dropDuplicates(["match_id"])
    )


def flatten_scorers(spark: SparkSession, bronze_path: str) -> DataFrame:
    df = spark.read.option("multiline", "true").json(bronze_path)
    df = df.select(
        F.col("competition.id").alias("competition_id"),
        F.col("competition.name").alias("competition_name"),
        F.explode("scorers").alias("scorer"),
    )
    return (
        df.select(
            F.col("competition_id"),
            F.col("competition_name"),
            F.col("scorer.player.id").alias("player_id"),
            F.col("scorer.player.name").alias("player_name"),
            F.col("scorer.player.dateOfBirth").alias("date_of_birth"),
            F.col("scorer.player.nationality").alias("nationality"),
            F.col("scorer.player.section").alias("position"),
            F.col("scorer.team.id").alias("team_id"),
            F.col("scorer.team.name").alias("team_name"),
            F.col("scorer.playedMatches").alias("played_matches"),
            F.col("scorer.goals").alias("goals"),
            F.col("scorer.assists").alias("assists"),
            F.col("scorer.penalties").alias("penalties"),
        )
        .withColumn("ingested_at", F.current_timestamp())
        .filter(F.col("player_id").isNotNull())
        .dropDuplicates(["player_id"])
    )


def flatten_standings(spark: SparkSession, bronze_path: str) -> DataFrame:
    df = spark.read.option("multiline", "true").json(bronze_path)
    df = df.select(
        F.col("competition.id").alias("competition_id"),
        F.col("competition.name").alias("competition_name"),
        F.col("season.id").alias("season_id"),
        F.col("season.startDate").alias("season_start"),
        F.col("season.endDate").alias("season_end"),
        F.explode("standings").alias("standing"),
    )
    # keep only the overall TOTAL table (not HOME/AWAY splits)
    df = df.filter(F.col("standing.type") == "TOTAL").select(
        F.col("competition_id"),
        F.col("competition_name"),
        F.col("season_id"),
        F.col("season_start"),
        F.col("season_end"),
        F.explode("standing.table").alias("entry"),
    )
    return (
        df.select(
            F.col("competition_id"),
            F.col("competition_name"),
            F.col("season_id"),
            F.col("season_start"),
            F.col("season_end"),
            F.col("entry.position").alias("position"),
            F.col("entry.team.id").alias("team_id"),
            F.col("entry.team.name").alias("team_name"),
            F.col("entry.playedGames").alias("played_games"),
            F.col("entry.won").alias("won"),
            F.col("entry.draw").alias("draw"),
            F.col("entry.lost").alias("lost"),
            F.col("entry.points").alias("points"),
            F.col("entry.goalsFor").alias("goals_for"),
            F.col("entry.goalsAgainst").alias("goals_against"),
            F.col("entry.goalDifference").alias("goal_difference"),
            F.col("entry.form").alias("form"),
        )
        .withColumn("ingested_at", F.current_timestamp())
        .filter(F.col("team_id").isNotNull())
        .dropDuplicates(["team_id"])
    )


def flatten_squad(spark: SparkSession, bronze_path: str) -> DataFrame:
    # each Bronze player file is one team with a squad[] array
    df = spark.read.option("multiline", "true").json(bronze_path)
    df = df.select(
        F.col("id").alias("team_id"),
        F.col("name").alias("team_name"),
        F.col("shortName").alias("team_short_name"),
        F.col("venue").alias("venue"),
        F.col("founded").alias("founded"),
        F.explode("squad").alias("player"),
    )
    return (
        df.select(
            F.col("team_id"),
            F.col("team_name"),
            F.col("team_short_name"),
            F.col("venue"),
            F.col("founded"),
            F.col("player.id").alias("player_id"),
            F.col("player.name").alias("player_name"),
            F.col("player.position").alias("position"),
            F.col("player.dateOfBirth").alias("date_of_birth"),
            F.col("player.nationality").alias("nationality"),
        )
        .withColumn("ingested_at", F.current_timestamp())
        .filter(F.col("player_id").isNotNull())
        .dropDuplicates(["player_id", "team_id"])
    )