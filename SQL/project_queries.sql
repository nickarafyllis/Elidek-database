#3.6

select  
concat(researcher.first_name,' ',researcher.last_name) as full_name, count(*) as active_project_number
FROM researcher
inner join works ON works.researcher_id=researcher.researcher_id
inner join project
on works.project_id=project.project_id
where(timestampdiff(year, date_of_birth,current_date())<40 
AND current_date()<project.enddate AND current_date()>project.startdate)
group by researcher.researcher_id
order by count(*) DESC

#3.7

SELECT executive_name, organisation_name, SUM(amount) as total_sum
FROM executive
JOIN project 
ON executive.executive_id=project.executive_id
JOIN organisation
ON project.organisation_id=organisation.organisation_id
GROUP BY executive_name 
ORDER BY SUM(amount) DESC
LIMIT 5;