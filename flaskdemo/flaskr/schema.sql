drop table if exists entriew;
create table entries(
    id integer primary key autoincrement,
    title string not null,
    text string not null
);
