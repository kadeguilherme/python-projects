USE ONGS;

CREATE TABLE ongs (
    id INTEGER not null auto_increment,
    founder varchar(100),
    ongname varchar(100),
    sector varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;


INSERT INTO ongs (founder,ongname, sector) VALUES ("Assistencia Social", 'Rede Cidada', 'A Rede Cidada é uma Entidade de Assistencia Social.');
INSERT INTO ongs (founder,ongname, sector) VALUES ("Cultura", 'CASA ARTE VIDA', "Desenvolvimento social local por meio de ações complementares à educação escolar");
