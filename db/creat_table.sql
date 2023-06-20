CREATE TABLE weather (
  time TIMESTAMPTZ NOT NULL,
  place text,
  weather jsonb
);

SELECT create_hypertable(
    'weather',
    'time');

CREATE INDEX ix_symbol_time ON weather (time DESC);