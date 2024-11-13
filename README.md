Install postgresql service

```
sudo apt install postgresql
```

start postgresql service

```
sudo service postgresql start
sudo service postgresql status
```

connect to postgresql as postgres default user

``` 
sudo -u postgres psql
```

create user with password
```
create user db_user with encrypted password '12345';
```

create three databases
```
create database asia_database;
create database america_database;
create database europe_database;
```

Provide enough privileges for the user to access the database
```
grant all privileges on database asia_database to db_user;
grant create on schema public to db_user;

```

Test if the user has privileges to create table in the database

```
set role db_user;
select currect_user;
CREATE TABLE cars1 (
  name VARCHAR(25),
  model VARCHAR(25),
  year INT
);

drop table cars1;

```