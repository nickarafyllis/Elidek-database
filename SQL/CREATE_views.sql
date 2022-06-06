CREATE VIEW projects_per_researcher
AS
select concat(researcher.first_name,' ',researcher.last_name) as full_name, project.title, project.amount, project.startdate, project.enddate
from researcher, works, project
where researcher.researcher_id=works.researcher_id
AND works.title=project.title
order by full_name,project.title;


CREATE VIEW projects_per_scientific_field
AS
select scientific_field.scientific_field_name, project.title
from scientific_field, project, has
where scientific_field.scientific_field_name = has.scientific_field_name
AND has.title = project.title
order by scientific_field.scientific_field_name, project.title;

#3.4  -- View
CREATE VIEW
projperyear (organisation_name, projectnum, year)
as 
select a.organisation_name, count(*), year(p.startdate) as year
from organisation a 
inner join project p 
on a.organisation_name = p.organisation_name
group by a.organisation_name, year 
having count(*)>9