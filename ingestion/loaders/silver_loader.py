import os

from pyspark.sql import SparkSession, DataFrame


class SilverLoader:
    def __init__(self, base_bronze: str = "data/bronze", base_silver: str = "data/silver"):
        self.base_bronze = base_bronze
        self.base_silver = base_silver
        self.spark = (
            SparkSession.builder.appName("SportsDataPlatform-Silver")
            .master("local[*]")
            .config("spark.sql.shuffle.partitions", "4")
            .getOrCreate()
        )
        self.spark.sparkContext.setLogLevel("WARN")

    def bronze_path(self, entity: str) -> str:
        return os.path.join(self.base_bronze, entity, "*.json")

    def write(self, df: DataFrame, entity: str) -> str:
        out_path = os.path.join(self.base_silver, entity)
        df.write.mode("overwrite").parquet(out_path)
        print(f"  Written → {out_path}  (rows: {df.count()})")
        return out_path

    def stop(self):
        self.spark.stop()


