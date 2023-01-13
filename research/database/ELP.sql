CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
NEW.updated_at = NOW();
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

	
-- Admin, Operations, users, not_assigned
create table public.groups(
	id uuid NOT NULL primary key default gen_random_uuid(),
	
	name character varying(10) UNIQUE NOT NULL,
	description character varying(255),

	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	
	is_deleted bool NOT NULL DEFAULT false,	
	deleted_at timestamp with time zone 
);



CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public.groups
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


-- Full time, Part time, Interns
create table public.employements(
	id uuid NOT NULL primary key default gen_random_uuid(),
	
	name character varying(10) UNIQUE NOT NULL,
	description character varying(255),

	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	
	is_deleted bool NOT NULL DEFAULT false,
	deleted_at timestamp with time zone 
);




CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public.employements
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

-- User1, User2
create table public.users(
	id uuid NOT NULL primary key default gen_random_uuid(),
	
	employee_id character varying(10),
	email_id character varying(255) NOT NULL,
	first_name character varying(50) NOT NULL,
	last_name character varying(50)NOT NULL,
	phone_number character varying(15) ,
	DOB date NOT NULL,
	gender character varying(2) ,
	designation character varying(15),
	
	group_id uuid NOT NULL,
	FOREIGN KEY(group_id) REFERENCES groups(id),
	
	employement_id uuid NOT NULL,
	FOREIGN KEY(employement_id) REFERENCES employements(id),
	
	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	
	is_deleted bool NOT NULL DEFAULT false,
	deleted_at timestamp with time zone 
);



CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public.users
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

-- reward1, reward2
create table public.rewards(
	id uuid NOT NULL primary key default gen_random_uuid(),
	
	title character varying(50) UNIQUE NOT NULL,
	description character varying(255),
	
	employement_id uuid NOT NULL,
	FOREIGN KEY(employement_id) REFERENCES employements(id),
	
	points int NOT NULL DEFAULT 0,
	
	is_expiry_date bool NOT NULL DEFAULT false,
	
	valid_from date NOT NULL,
	valid_till date,
	
	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
	
	is_deleted bool NOT NULL DEFAULT false,
	deleted_at timestamp with time zone 
);



CREATE TRIGGER set_timestamp
BEFORE UPDATE ON public.rewards
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

-- Full time person can access reward1 only
create table public.employement_rewards(
	id uuid NOT NULL primary key default gen_random_uuid(),
	
	employement_id uuid  NOT NULL,
	FOREIGN KEY (employement_id) REFERENCES employements(id),
	
	reward_id uuid NOT NULL NOT NULL,
	FOREIGN KEY (reward_id) REFERENCES rewards(id),
	
	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);




-- user1 recieved reward2
-- user1 recieved reward3
create table public.user_rewards(
	id uuid NOT NULL primary key default gen_random_uuid(),
	
	user_id uuid NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(id),
	
	reward_id uuid NOT NULL,
	FOREIGN KEY (reward_id) REFERENCES rewards(id),
	
	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);
