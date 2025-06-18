-- Docker's internal network
-- Uso de % en vez de localhost - docker internal network

CREATE DATABASE IF NOT EXISTS gestion_comercial;
USE gestion_comercial;

-- Read-only user
CREATE USER IF NOT EXISTS 'reader'@'%' IDENTIFIED BY 'reader_pass';
GRANT SELECT ON gestion_comercial.* TO 'reader'@'%';

-- Read-write user
CREATE USER IF NOT EXISTS 'writer'@'%' IDENTIFIED BY 'writer_pass';
GRANT SELECT, INSERT, UPDATE, DELETE ON gestion_comercial.* TO 'writer'@'%';