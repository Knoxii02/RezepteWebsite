DROP DATABASE IF EXISTS recipes;
CREATE DATABASE recipes;

USE recipes;

CREATE TABLE rezepte (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dauer INT NOT NULL,
    kalorien INT NOT NULL,
    zutaten VARCHAR(1024) NOT NULL,
    zubereitung VARCHAR(1024) NOT NULL
);

CREATE TABLE bugusers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    email_address VARCHAR(50) NOT NULL,
    password VARCHAR(60) NOT NULL
);

INSERT INTO bugusers (id, username, email_address, password) VALUES (1, 'Derk', 'de@alb.de', 'pass');
INSERT INTO bugusers (id, username, email_address, password) VALUES (2, 'Natalie', 'na@alb.de', 'pass');
INSERT INTO bugusers (id, username, email_address, password) VALUES (3, 'Anaking', 'an@alb.de', 'pass');

INSERT INTO rezepte (name, dauer, kalorien, zutaten, zubereitung) VALUES ('Spaghetti Carbonara', 25, 650, '400g Spaghetti, 200g Speck, 4 Eier, 100g Parmesan, Salz, Pfeffer', 'Spaghetti nach Packungsanleitung kochen. Speck in einer Pfanne knusprig braten. Eier mit geriebenem Parmesan verquirlen. Spaghetti abgießen, mit Speck vermischen und vom Herd nehmen. Ei-Käse-Mischung unterrühren. Mit Salz und Pfeffer abschmecken.');
INSERT INTO rezepte (name, dauer, kalorien, zutaten, zubereitung) VALUES ('Gemüsepfanne', 20, 320, '1 Paprika, 1 Zucchini, 200g Champignons, 2 Zwiebeln, 3 EL Olivenöl, Salz, Pfeffer, Kräuter', 'Gemüse waschen und in mundgerechte Stücke schneiden. Öl in einer großen Pfanne erhitzen. Zwiebeln glasig dünsten, dann restliches Gemüse hinzufügen. Bei mittlerer Hitze 15 Minuten braten. Mit Salz, Pfeffer und Kräutern würzen.');
INSERT INTO rezepte (name, dauer, kalorien, zutaten, zubereitung) VALUES ('Schokokuchen', 50, 420, '200g Butter, 200g Zucker, 4 Eier, 150g Mehl, 50g Kakao, 1 TL Backpulver, 100g Schokolade', 'Butter und Zucker schaumig rühren. Eier einzeln unterrühren. Mehl, Kakao und Backpulver mischen und unterheben. Gehackte Schokolade untermischen. In gefettete Form füllen. Bei 180°C ca. 35 Minuten backen.');
INSERT INTO rezepte (name, dauer, kalorien, zutaten, zubereitung) VALUES ('Tomatensuppe', 30, 180, '1kg Tomaten, 2 Zwiebeln, 2 Knoblauchzehen, 500ml Gemüsebrühe, 100ml Sahne, Olivenöl, Basilikum, Salz, Pfeffer', 'Zwiebeln und Knoblauch in Olivenöl andünsten. Gewürfelte Tomaten hinzufügen und 5 Minuten köcheln. Brühe zugießen, 15 Minuten kochen. Mit Pürierstab fein pürieren. Sahne einrühren, mit Salz und Pfeffer abschmecken. Mit Basilikum garnieren.');


