-- Silver layer: cleaned, typed, deduplicated data

CREATE TABLE IF NOT EXISTS silver.fixtures (
    fixture_id   INT          PRIMARY KEY,
    league_id    INT          NOT NULL,
    season       INT          NOT NULL,
    match_date   DATE         NOT NULL,
    home_team    VARCHAR(100) NOT NULL,
    away_team    VARCHAR(100) NOT NULL,
    home_goals   INT,
    away_goals   INT,
    status       VARCHAR(50),
    ingested_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS silver.players (
    player_id    INT          PRIMARY KEY,
    name         VARCHAR(200) NOT NULL,
    team_id      INT          NOT NULL,
    nationality  VARCHAR(100),
    age          INT,
    position     VARCHAR(50),
    ingested_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
