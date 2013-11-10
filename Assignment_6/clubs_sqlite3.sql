PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE club
                ( ident integer primary key,
                    name text,
                    description text,
                    president_id int,
                    foreign key (president_id) references person (ident)
                );
INSERT INTO "club" VALUES(106,'French','Pour les amateurs de la langue francaise',103);
INSERT INTO "club" VALUES(107,'German','Diejenigen, die Deutsch sprechen',102);
INSERT INTO "club" VALUES(108,'Rugby','Intercollegiate Rugby competition',101);
INSERT INTO "club" VALUES(109,'Field Hockey','Intramural Field Hockey competition',105);
CREATE TABLE person
                    (   ident integer primary key,
                        name text,
                        email text
                    );
INSERT INTO "person" VALUES(101,'Alice','alice@acme.com');
INSERT INTO "person" VALUES(102,'Bob','bob@nadir.org');
INSERT INTO "person" VALUES(103,'Carol','carol@zenith.net');
INSERT INTO "person" VALUES(104,'Dave','dave@acme.com');
INSERT INTO "person" VALUES(105,'Eve','eve@nadir.com');
CREATE TABLE `group`
                ( ident integer primary key,
                    name text,
                    description text
                );
INSERT INTO "group" VALUES(110,'International','Clubs interested in international culture');
INSERT INTO "group" VALUES(111,'Sports','Clubs involved with sports');
CREATE TABLE member_of
                ( person_id integer,
                  club_id integer,
                  foreign key (person_id) references person (ident),
                  foreign key (club_id) references club (ident)
                );
INSERT INTO "member_of" VALUES(101,106);
INSERT INTO "member_of" VALUES(103,106);
INSERT INTO "member_of" VALUES(105,106);
INSERT INTO "member_of" VALUES(102,107);
INSERT INTO "member_of" VALUES(104,107);
INSERT INTO "member_of" VALUES(101,108);
INSERT INTO "member_of" VALUES(102,108);
INSERT INTO "member_of" VALUES(103,108);
INSERT INTO "member_of" VALUES(102,109);
INSERT INTO "member_of" VALUES(104,109);
INSERT INTO "member_of" VALUES(105,109);
CREATE TABLE belong_to
                    ( club_id integer,
                        group_id integer,
                        foreign key (club_id) references club(ident),
                        foreign key (group_id) references `group`(ident)
                    );
INSERT INTO "belong_to" VALUES(106,110);
INSERT INTO "belong_to" VALUES(107,110);
INSERT INTO "belong_to" VALUES(108,110);
INSERT INTO "belong_to" VALUES(108,111);
INSERT INTO "belong_to" VALUES(109,111);
COMMIT;
