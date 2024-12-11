CREATE TABLE readings (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    temperature FLOAT NOT NULL,
    pressure FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- dummy data, just to test the client
INSERT INTO readings (temperature, pressure, humidity, created_at) VALUES 
(22.5, 1013, 50, NOW()),
(22.7, 1012.8, 49.5, NOW() - INTERVAL 30 SECOND),
(23.0, 1012.5, 48, NOW() - INTERVAL 90 SECOND);
