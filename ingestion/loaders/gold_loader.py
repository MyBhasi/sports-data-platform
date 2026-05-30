import os
from pyspark.sql import SparkSession, DataFrame
from sqlalchemy import create_engine, text


class GoldLoader:
    def __init__(self, base_silver: str = "data/silver", base_gold: str = "data/gold"):
        self.base_silver = base_silver
        self.base_gold = base_gold
        self.spark = (
            SparkSession.builder.appName("SportsDataPlatform-Gold")
            .master("local[*]")
            .config("spark.sql.shuffle.partitions", "4")
            .getOrCreate()
        )
        self.spark.sparkContext.setLogLevel("WARN")
        self._engine = self._pg_engine()

    def _pg_engine(self):
        return create_engine(
            "postgresql+psycopg2://sports_user:sports_pass@localhost:5432/sports_db",
            connect_args={"gssencmode": "disable"},
        )

    def silver(self, entity: str) -> DataFrame:
        path = os.path.join(self.base_silver, entity)
        return self.spark.read.parquet(path)

    def write(self, df: DataFrame, table: str) -> None:
        gold_path = os.path.join(self.base_gold, table)
        df.write.mode("overwrite").parquet(gold_path)
        print(f"  Parquet → {gold_path}  (rows: {df.count()})")

        pdf = df.toPandas()
        with self._engine.begin() as conn:
            conn.execute(text(f"TRUNCATE TABLE gold.{table}"))
        pdf.to_sql(table, self._engine, schema="gold", if_exists="append", index=False)
        print(f"  PostgreSQL → gold.{table}")

    def stop(self):
        self.spark.stop()
        self._engine.dispose()
