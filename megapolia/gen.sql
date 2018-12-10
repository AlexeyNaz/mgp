create table auth_group
(
  id   int auto_increment
    primary key,
  name varchar(80) not null,
  constraint name
    unique (name)
);

create table auth_user
(
  id           int auto_increment
    primary key,
  password     varchar(128) not null,
  last_login   datetime(6)  null,
  is_superuser tinyint(1)   not null,
  username     varchar(150) not null,
  first_name   varchar(30)  not null,
  last_name    varchar(150) not null,
  email        varchar(254) not null,
  is_staff     tinyint(1)   not null,
  is_active    tinyint(1)   not null,
  date_joined  datetime(6)  not null,
  constraint username
    unique (username)
);

create table auth_user_groups
(
  id       int auto_increment
    primary key,
  user_id  int not null,
  group_id int not null,
  constraint auth_user_groups_user_id_group_id_94350c0c_uniq
    unique (user_id, group_id),
  constraint auth_user_groups_group_id_97559544_fk_auth_group_id
    foreign key (group_id) references auth_group (id),
  constraint auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
    foreign key (user_id) references auth_user (id)
);

create table django_content_type
(
  id        int auto_increment
    primary key,
  app_label varchar(100) not null,
  model     varchar(100) not null,
  constraint django_content_type_app_label_model_76bd3d3b_uniq
    unique (app_label, model)
);

create table auth_permission
(
  id              int auto_increment
    primary key,
  name            varchar(255) not null,
  content_type_id int          not null,
  codename        varchar(100) not null,
  constraint auth_permission_content_type_id_codename_01ab375a_uniq
    unique (content_type_id, codename),
  constraint auth_permission_content_type_id_2f476e4b_fk_django_co
    foreign key (content_type_id) references django_content_type (id)
);

create table auth_group_permissions
(
  id            int auto_increment
    primary key,
  group_id      int not null,
  permission_id int not null,
  constraint auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    unique (group_id, permission_id),
  constraint auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
    foreign key (permission_id) references auth_permission (id),
  constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
    foreign key (group_id) references auth_group (id)
);

create table auth_user_user_permissions
(
  id            int auto_increment
    primary key,
  user_id       int not null,
  permission_id int not null,
  constraint auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
    unique (user_id, permission_id),
  constraint auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
    foreign key (permission_id) references auth_permission (id),
  constraint auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
    foreign key (user_id) references auth_user (id)
);

create table django_migrations
(
  id      int auto_increment
    primary key,
  app     varchar(255) not null,
  name    varchar(255) not null,
  applied datetime(6)  not null
);

create table django_session
(
  session_key  varchar(40) not null
    primary key,
  session_data longtext    not null,
  expire_date  datetime(6) not null
);

create index django_session_expire_date_a5c62663
  on django_session (expire_date);

create table megagames_activity
(
  id       int auto_increment
    primary key,
  code     varchar(16)   not null,
  `desc`   varchar(1024) not null,
  comment  varchar(1024) null,
  win      int           not null,
  play     int           not null,
  password varchar(16)   not null
);

create table megagames_player
(
  id        int auto_increment
    primary key,
  pid       varchar(4)  not null,
  login     varchar(32) not null,
  firstName varchar(32) not null,
  lastName  varchar(32) not null,
  sub       varchar(32) not null,
  age       int         not null
);

create table megagames_event
(
  id          int auto_increment
    primary key,
  `add`       int not null,
  activity_id int not null,
  player_id   int not null,
  constraint megagames_event_activity_id_169746ce_fk_megagames_activity_id
    foreign key (activity_id) references megagames_activity (id),
  constraint megagames_event_player_id_8b9c9877_fk_megagames_player_id
    foreign key (player_id) references megagames_player (id)
);



INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (18, 'kviz', 'КВИЗ/ Брехня', null, 6, 2, 'eaxr6s');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (19, 'humancheckers', 'Человеческие Шашки', null, 6, 2, 'wcmvxb');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (20, 'golf', 'Мини гольф', null, 6, 2, 'wlt7pk');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (21, 'velo', 'Велооркестр', null, 4, 2, '2tp9s6');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (22, 'mobracing', 'Командная игра «Гонки на мобильных телефонах»', null, 2, 1, 'oadw77');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (23, 'world', 'Интерактивная зона «Оживающий мир» ', null, 2, 2, 'yu7x7h');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (24, 'game', 'Game-zone', null, 2, 1, 'ovz8r2');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (25, 'megacheckers', 'Горячительные Мегашашки', null, 2, 1, 'br2v04');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (26, 'poligon', 'Мастер-класс по полигональным маскам компьютерных персонажей', null, 6, 6, '9sdtmp');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (27, 'bar', 'Мастер-класс по приготовлению коктейлей', null, 1, 1, 'kr9jz7');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (28, 'fly', 'Мастер-класс по флейрингу', null, 2, 2, '1mbtl0');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (29, 'freeze', 'Крио-бар', null, 1, 1, 'tkiciq');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (30, 'spin', 'Видео Спиннер с оформлением в стилистике Мегафон ', null, 0, 0, 'of3wzq');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (31, 'master', 'Мастер игры ', null, 2, 1, 'sr676m');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (32, 'vr', 'VR очки', null, 1, 1, 'ymk0ao');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (33, 'foto', 'Фотобудка с масками Instagram/ Megagram', null, 0, 0, 'gymn0k');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (34, 'spheroracing', 'Гонки на роботизированных шариках Sphero', '2 часа/ http://picsbox.ru/gonki-rabotizirovannymi-sharami-sphero/', 4, 2, 'wk3ycq');
INSERT INTO db_mgp.megagames_activity (id, code, `desc`, comment, win, play, password) VALUES (35, 'sqracing', 'Гонки на гироскутере – 2 дорожки', ' конусы', 4, 2, 'cqcx5l');