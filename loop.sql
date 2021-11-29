--select * from app
--create table app_copy as select * from app
--select * from app_copy

do $$
declare
	app_name    app_copy.app_name%type;
	publisher   app_copy.publisher%type;
	price       app_copy.price%type;
	description app_copy.description%type;
	app_size    app_copy.app_size%type;
	category    app_copy.category%type;
	age_rating  app_copy.age_rating%type;
	
begin 
	app_name := 'SuperExtraCool App';
	publisher := 'Me Myself and I';
	price := 13;
	description := 'Test data';
	app_size := 200;
	category := 'Music';
	age_rating := 'For ages 3 and up';
	
	for counter in 1..3
		loop
			insert into app_copy(app_name, publisher, price, description, app_size, category, age_rating)
			values (app_name || counter, publisher || counter, price+counter, description|| counter, app_size+counter, category, age_rating);
		end loop;
end;
$$
	
