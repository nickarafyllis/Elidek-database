/* =====================
	CREATE DATABASE 
======================*/
DROP DATABASE IF EXISTS `HFRIManagement`;
CREATE DATABASE `HFRIManagement`;
ALTER DATABASE HFRIManagement
CHARACTER SET utf8
COLLATE utf8_bin;

/* =====================
	CREATE ENTITIES 
======================*/
USE `HFRIManagement`;

DROP TABLE IF EXISTS program;
CREATE TABLE program
(
    program_name varchar (50) PRIMARY KEY not null,
    directorate varchar (100)
);

DROP TABLE IF EXISTS scientific_field;
CREATE TABLE scientific_field
(
    scientific_field_name varchar (50) PRIMARY KEY not null
);

DROP TABLE IF EXISTS executive;
CREATE TABLE executive
(
    executive_name varchar (50) PRIMARY KEY not null
);

DROP TABLE IF EXISTS assessment;
CREATE TABLE assessment
(
    assessment_id int auto_increment PRIMARY KEY NOT NULL,
    grade int not null,
    assessment_date date
);

DROP TABLE IF EXISTS organisation;
CREATE TABLE organisation
(
    organisation_name varchar (50) PRIMARY KEY not null,
    abbreviation varchar (10),
    postal_code varchar (50),
    street varchar (50),
    city varchar (50)
    
);

DROP TABLE IF EXISTS company;
CREATE TABLE company
(
    organisation_name varchar (50) PRIMARY KEY NOT NULL, 
    own_funds int not null,
    FOREIGN KEY (organisation_name) REFERENCES  organisation(organisation_name) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS university;
CREATE TABLE university
(
    organisation_name varchar (50) PRIMARY KEY NOT NULL,
    budget_ministry int not null,
    FOREIGN KEY (organisation_name) REFERENCES  organisation(organisation_name) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS research_center;
CREATE TABLE research_center
(
    organisation_name varchar (50) PRIMARY KEY NOT NULL,
    budget_ministry int not null,
    budget_private_actions int not null,
    FOREIGN KEY (organisation_name) REFERENCES  organisation(organisation_name) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS phone;
CREATE TABLE phone
(
    phone_number varchar (50) PRIMARY KEY NOT NULL,
    organisation_name varchar (50) NOT NULL,
    FOREIGN KEY (organisation_name) REFERENCES organisation(organisation_name) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS researcher;
CREATE TABLE researcher
(
    researcher_id int auto_increment PRIMARY KEY NOT NULL,
    first_name varchar (50) not null, 
    last_name varchar (50) not null, 
    sex varchar (12) not null, 
    date_of_birth date,
    /*age int GENERATED ALWAYS AS (TIMESTAMPDIFF(YEAR, date_of_birth, current_date())),*/ /*mono sta queries ta derived*/
    employment_date date,
    organisation_name varchar (50) ,
    FOREIGN KEY (organisation_name) REFERENCES organisation(organisation_name) ON DELETE SET NULL ON UPDATE CASCADE
);

DROP TABLE IF EXISTS project;
CREATE TABLE project
(
	title varchar (50) PRIMARY KEY not null, 
    summary varchar (1000),
    amount int CHECK (amount>=100000 AND amount<=1000000),
    startdate date,
    enddate date,
    program_name varchar(50),
    organisation_name varchar (50),
    executive_name varchar(50),
    supervisor_id int,
    assessor_id int,
    assessment_id int,
    CONSTRAINT duration CHECK ((timestampdiff(year,startdate, enddate))>=1 and (timestampdiff(year,enddate, startdate))<=4),
    FOREIGN KEY (program_name) REFERENCES program(program_name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (organisation_name) REFERENCES organisation(organisation_name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (executive_name) REFERENCES executive(executive_name) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (supervisor_id)  REFERENCES researcher(researcher_id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (assessor_id) REFERENCES researcher(researcher_id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id) ON DELETE SET NULL ON UPDATE CASCADE
);

DROP TABLE IF EXISTS has;
CREATE TABLE has
(
    title varchar(50) NOT NULL,
    scientific_field_name varchar(50) NOT NULL,
    PRIMARY KEY (title,scientific_field_name),
    FOREIGN KEY (title) REFERENCES project(title) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (scientific_field_name) REFERENCES scientific_field(scientific_field_name) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS deliverable;
CREATE TABLE deliverable
(
    deliverable_id int auto_increment PRIMARY KEY NOT NULL, 
	deliverable_title varchar (50) not null, 
    summary varchar (500),
    delivery_date date,
    title varchar(50) NOT NULL,
    FOREIGN KEY (title) REFERENCES project(title) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS works;
CREATE TABLE works
(
    /*working_researcher_id int auto_increment PRIMARY KEY NOT NULL,*/
    #works_id int auto_increment PRIMARY KEY NOT NULL,
    researcher_id int NOT NULL,
    title varchar(50) NOT NULL, 
    PRIMARY KEY (researcher_id, title),
    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (title) REFERENCES project(title) ON DELETE CASCADE ON UPDATE CASCADE
);