--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3 (Debian 16.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: records; Type: TABLE; Schema: public; Owner: userdb123321
--

CREATE TABLE public.records (
    id integer NOT NULL,
    user_id integer NOT NULL,
    username character varying,
    user_role character varying NOT NULL,
    bot_token character varying NOT NULL,
    chat_id character varying NOT NULL,
    message text NOT NULL,
    telegram_response text
);


ALTER TABLE public.records OWNER TO userdb123321;

--
-- Name: records_id_seq; Type: SEQUENCE; Schema: public; Owner: userdb123321
--

CREATE SEQUENCE public.records_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.records_id_seq OWNER TO userdb123321;

--
-- Name: records_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: userdb123321
--

ALTER SEQUENCE public.records_id_seq OWNED BY public.records.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: userdb123321
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    role character varying NOT NULL
);


ALTER TABLE public.users OWNER TO userdb123321;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: userdb123321
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO userdb123321;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: userdb123321
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: records id; Type: DEFAULT; Schema: public; Owner: userdb123321
--

ALTER TABLE ONLY public.records ALTER COLUMN id SET DEFAULT nextval('public.records_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: userdb123321
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: records; Type: TABLE DATA; Schema: public; Owner: userdb123321
--

COPY public.records (id, user_id, username, user_role, bot_token, chat_id, message, telegram_response) FROM stdin;
1	1	Test1	user	6503074282:AAGwvcfDGyXJKASzAU72uDIULmRZesOygBo	7128321509	Hello World	{"ok": true, "result": {"message_id": 8, "from": {"id": 6503074282, "is_bot": true, "first_name": "iditenahuybot", "username": "ItitdeNahuyBot"}, "chat": {"id": 7128321509, "first_name": "\\u0414\\u043c\\u0438\\u0442\\u0440\\u043e", "username": "wizex375", "type": "private"}, "date": 1718453317, "text": "Hello World"}}
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: userdb123321
--

COPY public.users (id, username, password, role) FROM stdin;
1	Test1	$2b$12$fooCjIBOJXeplpg0Y1SOiuGfxmVQxAYPcJRYszYSaIjBTNG9VuV4a	user
\.


--
-- Name: records_id_seq; Type: SEQUENCE SET; Schema: public; Owner: userdb123321
--

SELECT pg_catalog.setval('public.records_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: userdb123321
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: records records_pkey; Type: CONSTRAINT; Schema: public; Owner: userdb123321
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: userdb123321
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_records_id; Type: INDEX; Schema: public; Owner: userdb123321
--

CREATE INDEX ix_records_id ON public.records USING btree (id);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: userdb123321
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: userdb123321
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: records records_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: userdb123321
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

