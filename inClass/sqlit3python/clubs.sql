PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE memberof
                ( personId int,
                  clubId int,
                  foreign key (personId) references person (ident),
                  foreign key (clubId) references person (ident)
                );
CREATE TABLE clubgroup
                ( ident int primary key,
                    name text,
                    description text
                );
INSERT INTO "clubgroup" VALUES(110,'International','Clubs interested in international culture');
INSERT INTO "clubgroup" VALUES(111,'Sports','Clubs involved with sports');
CREATE TABLE club
                ( ident int primary key,
                    name text,
                    description text,
                    president int,
                    foreign key (president) references person (ident)
                );
INSERT INTO "club" VALUES(106,'French','Pour les amateurs de la langue francaise',103);
INSERT INTO "club" VALUES(107,'German','Diejenigen, die Deutsch sprechen',102);
INSERT INTO "club" VALUES(108,'Rugby','Intercollegiate Rugby competition',101);
INSERT INTO "club" VALUES(109,'Field Hockey','Intramural Field Hockey competition',105);
CREATE TABLE person
                    (   ident int primary key,
                        name text,
                        email text
                    );
INSERT INTO "person" VALUES(101,'Alice','alice@acme.com');
INSERT INTO "person" VALUES(102,'Bob','bob@nadir.org');
INSERT INTO "person" VALUES(103,'Carol','carol@zenith.net');
INSERT INTO "person" VALUES(104,'Dave','dave@acme.com');
INSERT INTO "person" VALUES(105,'Eve','eve@nadir.com');
CREATE TABLE `group`
                ( ident int primary key,
                    name text,
                    description text
                );
INSERT INTO "group" VALUES(110,'International','Clubs interested in international culture');
INSERT INTO "group" VALUES(111,'Sports','Clubs involved with sports');
CREATE TABLE member_of
                ( personId int,
                  clubId int,
                  foreign key (personId) references person (ident),
                  foreign key (clubId) references club (ident)
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
                    ( club_id int,
                        group_id int,
                        foreign key (club_id) references club(ident),
                        foreign key (group_id) references `group`(ident)
                    );
INSERT INTO "belong_to" VALUES(106,110);
INSERT INTO "belong_to" VALUES(107,110);
INSERT INTO "belong_to" VALUES(108,110);
INSERT INTO "belong_to" VALUES(108,111);
INSERT INTO "belong_to" VALUES(109,111);
COMMIT;
