/* =====================
	CREATE DATABASE 
======================*/
DROP DATABASE IF EXISTS `HFRIManagement`;
CREATE DATABASE `HFRIManagement`;
ALTER DATABASE HFRIManagement
CHARACTER SET utf8
COLLATE utf8_bin; /*Greek_CI_AI;*/

/* =====================
	CREATE ENTITIES 
======================*/
USE `HFRIManagement`;

DROP TABLE IF EXISTS program;
CREATE TABLE program
(
    program_id int auto_increment PRIMARY KEY NOT NULL,
    program_name varchar (50) unique not null,
    directorate varchar (100)
);

DROP TABLE IF EXISTS scientific_field;
CREATE TABLE scientific_field
(
    scientific_field_id int auto_increment PRIMARY KEY NOT NULL,
    scientific_field_name varchar (50) unique not null
);

DROP TABLE IF EXISTS executive;
CREATE TABLE executive
(
    executive_id int auto_increment PRIMARY KEY NOT NULL,
    executive_name varchar (50) unique not null
);

DROP TABLE IF EXISTS assessment;
CREATE TABLE assessment
(
    assessment_id int auto_increment PRIMARY KEY NOT NULL,
    grade int not null,
    assessment_date date
);

DROP TABLE IF EXISTS location_address;
CREATE TABLE location_address
(
    location_address_id int auto_increment PRIMARY KEY NOT NULL,
    postal_code varchar (50),
    street varchar (50),
    city varchar (50)
);

DROP TABLE IF EXISTS organisation;
CREATE TABLE organisation
(
    organisation_id int auto_increment PRIMARY KEY NOT NULL,
    organisation_name varchar (50) unique not null,
    abbreviation varchar (10),
    location_address_id int NOT NULL,
    FOREIGN KEY (location_address_id) REFERENCES location_address(location_address_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS company;
CREATE TABLE company
(
    organisation_id int auto_increment PRIMARY KEY NOT NULL, 
    own_funds int not null,
    FOREIGN KEY (organisation_id) REFERENCES  organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS university;
CREATE TABLE university
(
    organisation_id int auto_increment PRIMARY KEY NOT NULL,
    budget_ministry int not null,
    FOREIGN KEY (organisation_id) REFERENCES  organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS research_center;
CREATE TABLE research_center
(
    organisation_id int auto_increment PRIMARY KEY NOT NULL,
    budget_ministry int not null,
    budget_private_actions int not null,
    FOREIGN KEY (organisation_id) REFERENCES  organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS phone;
CREATE TABLE phone
(
    phone_id int auto_increment PRIMARY KEY NOT NULL,
    phone_number varchar (50) unique NOT NULL,
    organisation_id int NOT NULL,
    FOREIGN KEY (organisation_id) REFERENCES organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS researcher;
CREATE TABLE researcher
(
    researcher_id int auto_increment PRIMARY KEY NOT NULL,
    first_name varchar (50) not null, 
    last_name varchar (50) not null, 
    sex varchar (6) not null, 
    date_of_birth date,
    /*age int GENERATED ALWAYS AS (TIMESTAMPDIFF(YEAR, date_of_birth, current_date())),*/ /*mono sta queries ta derived*/
    employment_date date,
    organisation_id int NOT NULL,
    FOREIGN KEY (organisation_id) REFERENCES organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS project;
CREATE TABLE project
(
	project_id int auto_increment PRIMARY KEY NOT NULL, 
	title varchar (50) unique not null, 
    summary varchar (500),
    amount int CHECK (amount>=100000 AND amount<=1000000),
    startdate date,
    enddate date,
    duration int, /*as (TIMESTAMPDIFF(YEAR, startdate, enddate)) CHECK (duration>0 AND duration<5), */
    program_id int NOT NULL,
    organisation_id int NOT NULL,
    executive_id int NOT NULL,
    supervisor_id int NOT NULL,
    assessor_id int NOT NULL,
    assessment_id int NOT NULL,
    FOREIGN KEY (program_id) REFERENCES program(program_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (organisation_id) REFERENCES organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (executive_id) REFERENCES executive(executive_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (supervisor_id)  REFERENCES researcher(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (assessor_id) REFERENCES researcher(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS has;
CREATE TABLE has
(
    has_id int auto_increment PRIMARY KEY NOT NULL,
    project_id int NOT NULL,
    scientific_field_id int NOT NULL,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (scientific_field_id) REFERENCES scientific_field(scientific_field_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS deliverable;
CREATE TABLE deliverable
(
    deliverable_id int auto_increment PRIMARY KEY NOT NULL, 
	title varchar (50) not null, 
    summary varchar (500),
    delivery_date date,
    project_id int NOT NULL,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

DROP TABLE IF EXISTS works;
CREATE TABLE works
(
    /*working_researcher_id int auto_increment PRIMARY KEY NOT NULL,*/
    works_id int auto_increment PRIMARY KEY NOT NULL,
    researcher_id int NOT NULL,
    project_id int NOT NULL, 
    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE RESTRICT ON UPDATE CASCADE
);