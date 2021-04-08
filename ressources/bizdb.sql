create table Feeds (

    feed_id integer not null  primary key autoincrement,
    description varchar(200) null,
    link varchar(100) not null
    
);

create table Items (

    item_id integer not null primary key autoincrement,
    title varchar(200) not null,
    links varchar(200) not null,
    pub_date datetime not null,
    content text not null,
    feed_id int not null,

    foreign key (feed_id) references Feeds(feed_id)

);