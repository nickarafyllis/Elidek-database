/* =====================
	CREATE DATABASE 
======================*/
CREATE DATABASE IF NOT EXISTS `HFRIManagement`;
ALTER DATABASE HFRIManagement
CHARACTER SET utf8
COLLATE Greek_CI_AI;

/* =====================
	CREATE ENTITIES 
======================*/
USE `HFRIManagement`;

CREATE TABLE IF NOT EXISTS program
(
    program_id int auto_increment PRIMARY KEY NOT NULL,
    program_name varchar (50) not null,
    management varchar (50)
);

CREATE TABLE IF NOT EXISTS scientific_field
(
    scientific_field_id int auto_increment PRIMARY KEY NOT NULL,
    scientific_field_name varchar (50) not null
);

CREATE TABLE IF NOT EXISTS executive
(
    executive_id int auto_increment PRIMARY KEY NOT NULL,
    executive_name varchar (50) not null
);

CREATE TABLE IF NOT EXISTS assessment
(
    assessment_id int auto_increment PRIMARY KEY NOT NULL,
    grade int not null,
    assessment_date date
);

CREATE TABLE IF NOT EXISTS location_address
(
    location_address_id int auto_increment PRIMARY KEY NOT NULL,
    postal_code varchar (50),
    street varchar (50),
    city varchar (50)
);

CREATE TABLE IF NOT EXISTS company
(
    company_id int auto_increment PRIMARY KEY NOT NULL,
    own_funds int not null
);

CREATE TABLE if not exists university
(
    university_id int auto_increment PRIMARY KEY NOT NULL,
    budget_ministry int not null
);

CREATE TABLE IF NOT EXISTS research_center
(
    research_center_id int auto_increment PRIMARY KEY NOT NULL,
    budget_ministry int not null,
    budget_private_actions int not null
);

CREATE TABLE IF NOT EXISTS organisation_type
(
   organisation_type_id int auto_increment PRIMARY KEY NOT NULL,
   university_id int NOT NULL,
   company_id int NOT NULL,
   research_center_id int NOT NULL,
   FOREIGN KEY (company_id) REFERENCES company(company_id) ON DELETE RESTRICT ON UPDATE CASCADE,
   FOREIGN KEY (university_id) REFERENCES university(university_id) ON DELETE RESTRICT ON UPDATE CASCADE,
   FOREIGN KEY (research_center_id) REFERENCES research_center(research_center_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS organisation
(
    organisation_id int auto_increment PRIMARY KEY NOT NULL,
    organisation_name varchar (50) not null,
    abbreviation varchar (10),
    organisation_type_id int NOT NULL,
    location_address_id int NOT NULL,
    FOREIGN KEY (organisation_type_id) REFERENCES organisation_type(organisation_type_id) ON DELETE RESTRICT ON UPDATE CASCADE, /*den eimai sigouros edo*/
    FOREIGN KEY (location_address_id) REFERENCES location_address(location_address_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS phone
(
    phone_id int auto_increment PRIMARY KEY NOT NULL,
    phone_number varchar (50),
    organisation_id int NOT NULL,
    FOREIGN KEY (organisation_id) REFERENCES organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS researcher
(
    researcher_id int auto_increment PRIMARY KEY NOT NULL,
    first_name varchar (50) not null, 
    last_name varchar (50) not null, 
    sex varchar (10) not null, 
    age int not null,
    date_of_birth date,
    employment_date date,
    organisation_id int NOT NULL,
    FOREIGN KEY (organisation_id) REFERENCES organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS project
(
	project_id int auto_increment PRIMARY KEY NOT NULL, 
	title varchar (50) not null, 
    summary varchar (500),
    amount int CHECK (amount>=100000 AND amount<=1000000),
    startdate date,
    enddate date,
    duration int CHECK (duration>0 AND duration<5), 
    scientific_field_id int NOT NULL,
    program_id int NOT NULL,
    organisation_id int NOT NULL,
    executive_id int NOT NULL,
    supervisor_id int NOT NULL,
    assessor_id int NOT NULL,
    assessment_id int NOT NULL,
    FOREIGN KEY (scientific_field_id) REFERENCES scientific_field(scientific_field_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (program_id) REFERENCES program(program_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (organisation_id) REFERENCES organisation(organisation_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (executive_id) REFERENCES executive(executive_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (supervisor_id)  REFERENCES researcher(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (assessor_id) REFERENCES researcher(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS deliverable
(
    deliverable_id int auto_increment PRIMARY KEY NOT NULL, 
	title varchar (50) not null, 
    summary varchar (500),
    delivery_date date,
    project_id int NOT NULL,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS working_researcher
(
    /*working_researcher_id int auto_increment PRIMARY KEY NOT NULL,*/
    researcher_id int NOT NULL,
    project_id int NOT NULL, 
    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE RESTRICT ON UPDATE CASCADE
);