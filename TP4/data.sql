CREATE DATABASE demosql;
USE demosql;
CREATE TABLE myTable(id int AUTO_INCREMENT, name varcgar(45) NOT FULL, PRIMARY KEY (id));
INSERT INTO myTable (id, name) VALUES (NULL, 'bob');
INSERT INTO myTable (id, name) VALUES (NULL, 'alice');
INSERT INTO myTable (id, name) VALUES (NULL, 'john');
