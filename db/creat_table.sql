CREATE TABLE weather (
  time TIMESTAMPTZ NOT NULL,
  temp real,
  pressure real,
  humidity real,
  wind jsonb
);

SELECT create_hypertable(
    'weather',
    'time');

CREATE INDEX ix_symbol_time ON weather (time DESC);