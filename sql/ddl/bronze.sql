-- Bronze layer: raw ingested data (append-only, no transformation)

CREATE TABLE IF NOT EXISTS bronze.raw_fixtures (
    id          SERIAL PRIMARY KEY,
    raw_json    JSONB        NOT NULL,
    source      VARCHAR(50)  NOT NULL DEFAULT 'api-football',
    ingested_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS bronze.raw_standings (
    id          SERIAL PRIMARY KEY,
    raw_json    JSONB        NOT NULL,
    source      VARCHAR(50)  NOT NULL DEFAULT 'api-football',
    ingested_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS bronze.raw_players (
    id          SERIAL PRIMARY KEY,
    raw_json    JSONB        NOT NULL,
    source      VARCHAR(50)  NOT NULL DEFAULT 'api-football',
    ingested_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
