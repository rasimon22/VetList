CREATE TABLE users(user_id int AUTO_INCREMENT,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	serial_number varchar(20),
	branch tinyint NOT NULL,
	social_security_number int NOT NULL,
	uso_status smallint NOT NULL,
	PRIMARY KEY(user_id));

CREATE TABLE experience(exp_id int AUTO_INCREMENT,
	user_id int NOT NULL,
	company varchar(255) NOT NULL,
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	responsibilities TEXT,
	military BOOLEAN,
	PRIMARY KEY (exp_id));

CREATE TABLE skills(skill_id int AUTO_INCREMENT,
	user_id int NOT NULL,
	skill varchar(255) NOT NULL,
	proficiency int NOT NULL,
	PRIMARY KEY (skill_id));

CREATE TABLE employer(employer_id int AUTO_INCREMENT,
	name varchar(255) NOT NULL,
	zip_code MEDIUMINT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (employer_id));

CREATE TABLE listings(listing_id int AUTO_INCREMENT,
	employer_id int NOT NULL,
	zip_code MEDIUMINT NOT NULL,
	openings int NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (listing_id));
ALTER TABLE experience ADD FOREIGN KEY(user_id) REFERENCES users(user_id);
ALTER TABLE skills ADD FOREIGN KEY (user_id) REFERENCES users(user_id);
ALTER TABLE listings ADD FOREIGN KEY(employer_id) REFERENCES employer(employer_id);
