#leipoun 3.4 3.5miso 

#3.1 

#1. 
select program.program_name
from program;

#2

#a
select title
from project
join program
on project.program_name=program.program_name
where program.program_name='Euratom' -- parametros
order by enddate - startdate desc

#b
select title
from project
join program
on project.program_name=program.program_name
where program.program_name='Euratom' -- parametros
order by startdate desc

#c
select title
from project
join program
on project.program_name=program.program_name
join executive
on project.executive_name=executive.executive_name
where program.program_name='Euratom'  -- parametros 
order by executive.executive_name
#3
select concat(researcher.first_name,' ',researcher.last_name) as full_name
from researcher 
join works
on researcher.researcher_id=works.researcher_id
join project
on works.title=project.title
where project.title='proj2' -- parametros

#3.3
1.
select project.title
from project
inner join hasz
on project.title=has.title
where(current_date()<project.enddate AND current_date()>project.startdate AND has.scientific_field_name='Nuclear physics');

2.
select concat(researcher.first_name,' ',researcher.last_name) as full_name
from researcher
inner join works
on researcher.researcher_id=works.researcher_id
inner join has
on works.title= has.title
join project
on project.title=has.title
where(current_date()<project.enddate AND current_date()>project.startdate AND timestampdiff(year,startdate, current_date())<1 AND has.scientific_field_name='Nuclear physics');

#3.5 
SELECT A.scientific_field_name AS scientificfield1, B.scientific_field_name AS scientificfield2, count(*)
FROM has A, has B
WHERE A.title = B.title
and A.scientific_field_name <> B.scientific_field_name
and B.scientific_field_name > A.scientific_field_name
GROUP by A.scientific_field_name, B.scientific_field_name 
ORDER BY count(*) desc

#3.6
select  
researcher.first_name, researcher.last_name, count(*) as active_project_number
FROM researcher
inner join works ON works.researcher_id=researcher.researcher_id
inner join project
on works.title=project.title
where(timestampdiff(year, date_of_birth,current_date())<40 
AND current_date()<project.enddate AND current_date()>project.startdate)
group by researcher.researcher_id
order by count(*) DESC
limit 3

#3.7
SELECT executive.executive_name , organisation.organisation_name, SUM(amount)
FROM executive
JOIN project 
ON executive.executive_name=project.executive_name
JOIN organisation 
ON project.organisation_name=organisation.organisation_name
JOIN company 
on organisation.organisation_name=company.organisation_name
where own_funds<>0
GROUP BY executive_name
ORDER BY SUM(amount) 
DESC LIMIT 5;

#3.8
select concat(researcher.first_name,' ',researcher.last_name) as full_name , count(*) 
from researcher 
join works 
on works.researcher_id = researcher.researcher_id 
where works.title in ( 
    SELECT DISTINCT project.title
    FROM project 
    WHERE project.title not in (select title from deliverable)
) 
group by works.researcher_id
having count(*)>4
order by count(*) desc;