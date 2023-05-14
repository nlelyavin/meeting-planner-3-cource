INSERT INTO weekday (name)
SELECT 'Monday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Monday'
        );

INSERT INTO weekday (name)
SELECT 'Tuesday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Tuesday'
        );

INSERT INTO weekday (name)
SELECT 'Wednesday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Wednesday'
        );

INSERT INTO weekday (name)
SELECT 'Thursday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Thursday'
        );

INSERT INTO weekday (name)
SELECT 'Friday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Friday'
        );

INSERT INTO weekday (name)
SELECT 'Saturday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Saturday'
        );

INSERT INTO weekday (name)
SELECT 'Sunday'
WHERE
    NOT EXISTS (
            SELECT name FROM weekday WHERE name = 'Sunday'
        );