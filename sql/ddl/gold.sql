-- Gold layer: business-ready aggregations

CREATE TABLE IF NOT EXISTS gold.top_scorers (
    player_id         INT          NOT NULL,
    player_name       VARCHAR(200) NOT NULL,
    team_name         VARCHAR(100) NOT NULL,
    competition_name  VARCHAR(100) NOT NULL,
    total_goals       INT          NOT NULL DEFAULT 0,
    total_assists     INT          NOT NULL DEFAULT 0,
    total_penalties   INT          NOT NULL DEFAULT 0,
    updated_at        TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    PRIMARY KEY (player_id, competition_name)
);

CREATE TABLE IF NOT EXISTS gold.team_standings (
    team_id             INT          NOT NULL,
    team_name           VARCHAR(100) NOT NULL,
    competition_name    VARCHAR(100) NOT NULL,
    total_wins          INT          NOT NULL DEFAULT 0,
    total_draws         INT          NOT NULL DEFAULT 0,
    total_losses        INT          NOT NULL DEFAULT 0,
    total_goals_for     INT          NOT NULL DEFAULT 0,
    total_goals_against INT          NOT NULL DEFAULT 0,
    total_points        INT          NOT NULL DEFAULT 0,
    updated_at          TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    PRIMARY KEY (team_id, competition_name)
);

CREATE TABLE IF NOT EXISTS gold.match_results (
    match_id         INT          PRIMARY KEY,
    competition_name VARCHAR(100) NOT NULL,
    matchday         INT,
    match_date       DATE,
    home_team_name   VARCHAR(100) NOT NULL,
    away_team_name   VARCHAR(100) NOT NULL,
    full_time_home   INT,
    full_time_away   INT,
    winner           VARCHAR(50),
    referee_name     VARCHAR(200),
    updated_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS gold.referee_stats (
    referee_name          VARCHAR(200) PRIMARY KEY,
    referee_nationality   VARCHAR(100),
    matches_officiated    INT          NOT NULL DEFAULT 0,
    updated_at            TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
