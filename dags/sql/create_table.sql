CREATE TABLE IF NOT EXISTS egyptian_league_clubs (
    id SERIAL PRIMARY KEY,
    name_club VARCHAR(100) NOT NULL,
    year_of_construction INT NOT NULL,
    degree_of_level_league VARCHAR(50) NOT NULL,
    num_of_trophy INT NOT NULL
);
