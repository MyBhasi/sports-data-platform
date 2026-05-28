-- Gold layer: business-ready aggregations

CREATE TABLE IF NOT EXISTS gold.top_scorers (
    player_id    INT          PRIMARY KEY,
    player_name  VARCHAR(200) NOT NULL,
    team_name    VARCHAR(100) NOT NULL,
    total_goals  INT          NOT NULL DEFAULT 0,
    season       INT          NOT NULL,
    updated_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS gold.team_standings (
    team_id           INT          PRIMARY KEY,
    team_name         VARCHAR(100) NOT NULL,
    total_wins        INT          NOT NULL DEFAULT 0,
    total_draws       INT          NOT NULL DEFAULT 0,
    total_losses      INT          NOT NULL DEFAULT 0,
    total_goals_for   INT          NOT NULL DEFAULT 0,
    total_goals_against INT        NOT NULL DEFAULT 0,
    points            INT          NOT NULL DEFAULT 0,
    season            INT          NOT NULL,
    updated_at        TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
