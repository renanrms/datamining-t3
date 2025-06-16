CREATE TABLE IF NOT EXISTS public.vehicle_tracking
(
    ordem text COLLATE pg_catalog."default",
    latitude double precision,
    longitude double precision,
    datahora_epoch bigint,
    datahora timestamp without time zone,
    velocidade integer,
    linha text COLLATE pg_catalog."default",
    datahoraenvio_epoch bigint,
    datahoraservidor_epoch bigint,
    datahoraservidor timestamp without time zone,
    datahoraenvio timestamp without time zone,
    geom geography(Point,4326)
) PARTITION BY RANGE (datahora);
