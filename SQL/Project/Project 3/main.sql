CREATE TABLE news (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    source VARCHAR(50),
    score INT,
    comments_count INT,
    created_at DATETIME
);


INSERT INTO news (id, title, source, score, comments_count, created_at) VALUES
(1, 'AI beats humans in chess again', 'hacker_news', 120, 45, '2025-10-29 10:00:00'),
(2, 'New programming language released', 'hacker_news', 80, 30, '2025-10-28 09:00:00'),
(3, 'SpaceX launches new rocket', 'reddit', 200, 90, '2025-10-27 08:00:00'),
(4, 'Cybersecurity update for Linux', 'hacker_news', 95, 50, '2025-10-30 07:30:00'),
(5, 'Quantum computers are here', 'hacker_news', 150, 60, '2025-10-25 11:00:00');


SELECT *
FROM news
WHERE source = 'hacker_news';
