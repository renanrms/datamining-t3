CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS tracking (
    id SERIAL PRIMARY KEY,
    ordem text COLLATE pg_catalog."default",
    geom GEOGRAPHY(POINT, 4326),
    datahora TIMESTAMP NOT NULL,
    velocidade FLOAT,
    linha text COLLATE pg_catalog."default",
    datahoraenvio TIMESTAMP,
    datahoraservidor TIMESTAMP
);


CREATE INDEX IF NOT EXISTS idx_tracking_ordem ON tracking(ordem);
CREATE INDEX IF NOT EXISTS idx_tracking_linha ON tracking(linha);
CREATE INDEX IF NOT EXISTS idx_tracking_datahora ON tracking(datahora);
CREATE INDEX IF NOT EXISTS idx_tracking_geom ON tracking USING GIST(geom);
