-- creates a stored procedure that computes and store the average score for a student
-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the average score for the user
    IF EXISTS (SELECT 1 FROM average_scores WHERE user_id = user_id) THEN
        UPDATE average_scores
        SET average_score = avg_score
        WHERE user_id = user_id;
    ELSE
        INSERT INTO average_scores (user_id, average_score)
        VALUES (user_id, avg_score);
    END IF;
    
    
END //

DELIMITER ;
