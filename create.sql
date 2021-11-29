CREATE TABLE category (
	category VARCHAR(10) NOT NULL,
	PRIMARY KEY (category)
);

CREATE TABLE age_rating (
	age_rating VARCHAR(10) NOT NULL, 
	PRIMARY KEY (age_rating)
);

CREATE TABLE publisher (
	publisher VARCHAR(50) NOT NULL,
	PRIMARY KEY (publisher)
);

CREATE TABLE app (
	app_name VARCHAR(60) NOT NULL, 
	publisher VARCHAR(50) REFERENCES publisher(publisher),
	price FLOAT,
	description VARCHAR(500),
	app_size FLOAT,
	category VARCHAR(10) REFERENCES category(category),
	age_rating VARCHAR(10) REFERENCES age_rating(age_rating),
	PRIMARY KEY (app_name),
	FOREIGN KEY (category) REFERENCES category(category),
	FOREIGN KEY (age_rating) REFERENCES age_rating(age_rating)
);

CREATE TABLE app_publisher(
	app_name VARCHAR(60) REFERENCES app(app_name),
	publisher VARCHAR(50) REFERENCES publisher(publisher),
	initial_date_of_release DATE
);



