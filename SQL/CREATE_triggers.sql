DELIMITER $$
DROP TRIGGER IF EXISTS before_assessor_insert$$
CREATE TRIGGER before_assessor_insert
before insert ON project FOR EACH ROW
BEGIN
IF new.assessor_id in (select a.researcher_id from researcher a where new.organisation_name = a.organisation_name) 
THEN SIGNAL SQLSTATE '50001' SET MESSAGE_TEXT = 'Assessor cannot assess a project belonging in his organisation';
END IF;
END $$

DELIMITER $$
DROP TRIGGER IF EXISTS before_assessor_update$$
CREATE TRIGGER before_assessor_update
before update ON project FOR EACH ROW
BEGIN
IF new.assessor_id in (select a.researcher_id from researcher a where new.organisation_name = a.organisation_name) 
THEN SIGNAL SQLSTATE '50004' SET MESSAGE_TEXT = 'New assessor cannotassess a project belonging in his organisation';
END IF;
END $$
