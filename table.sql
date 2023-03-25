CREATE TABLE IF NOT EXISTS public."Employee"
(
    employee_id integer NOT NULL,
    name character varying(128) COLLATE pg_catalog."default" NOT NULL,
    email character varying(32) COLLATE pg_catalog."default" NOT NULL,
    password character varying(64) COLLATE pg_catalog."default" NOT NULL,
    phone_number character varying(32) COLLATE pg_catalog."default",
    work_experience integer,
    "position" character varying(32) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Employee_pkey" PRIMARY KEY (employee_id)
)

CREATE TABLE IF NOT EXISTS public."Review"
(
    review_id integer NOT NULL,
    user_id integer NOT NULL,
    employee_id integer NOT NULL,
    body character varying(1024) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Review_pkey" PRIMARY KEY (review_id),
    CONSTRAINT fk_employee_id FOREIGN KEY (employee_id)
        REFERENCES public."Employee" (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES public."User" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

CREATE TABLE IF NOT EXISTS public."Session"
(
    session_id integer NOT NULL,
    user_id integer NOT NULL,
    date date NOT NULL,
    description character varying(128) COLLATE pg_catalog."default",
    status character varying(32) COLLATE pg_catalog."default" NOT NULL,
    employee_id integer NOT NULL,
    sketch_id integer NOT NULL,
    CONSTRAINT "Session_pkey" PRIMARY KEY (session_id),
    CONSTRAINT fk_employee_id FOREIGN KEY (employee_id)
        REFERENCES public."Employee" (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_sketch_id FOREIGN KEY (sketch_id)
        REFERENCES public."Sketch" (sketch_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES public."User" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

CREATE TABLE IF NOT EXISTS public."Sketch"
(
    sketch_id integer NOT NULL,
    description character varying(128) COLLATE pg_catalog."default" NOT NULL,
    price real NOT NULL,
    CONSTRAINT "Sketch_pkey" PRIMARY KEY (sketch_id)
)

CREATE TABLE IF NOT EXISTS public."User"
(
    user_id integer NOT NULL,
    email character varying(32) COLLATE pg_catalog."default" NOT NULL,
    password character varying(64) COLLATE pg_catalog."default" NOT NULL,
    name character varying(128) COLLATE pg_catalog."default" NOT NULL,
    phone_number character varying(32) COLLATE pg_catalog."default",
    CONSTRAINT "User_pkey" PRIMARY KEY (user_id)
)
