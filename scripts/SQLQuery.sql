-- CREATE DATABASE AntiSocial;
/* Tabla usuario*/
CREATE TABLE Usuario (ID_usuario INT PRIMARY KEY auto_increment,
                      nombre_usuario VARCHAR (20) UNIQUE,
					  nombre VARCHAR(20) NOT NULL,
                      apellido VARCHAR (20) NOT NULL,
                      email VARCHAR(50) UNIQUE,
                      contrasena VARCHAR(15) NOT NULL,
                      fdenacimiento DATE,
                      telefono BIGINT,
                      sexo CHAR);

/* Tabla Publicaciones*/ 
CREATE TABLE Post (ID_post INT PRIMARY KEY NOT NULL auto_increment,
				   ID_usuario INT NOT NULL,
                   contenido TINYTEXT NOT NULL,
                   timestamp DATETIME NOT NULL,
                   FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario));
	
/* Tabla Comentarios*/
CREATE TABLE Comentario (ID_comentario INT PRIMARY KEY auto_increment,
						 ID_post INT,
                         ID_usuario INT,
                         contenido TINYTEXT NOT NULL,
                         timestamp DATETIME NOT NULL,
                         FOREIGN KEY (ID_post) REFERENCES Post(ID_post),
                         FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario));

/* Tabla de Likes */
CREATE TABLE Likes (ID_like INT  PRIMARY KEY auto_increment,
					ID_post INT,
                    ID_usuario INT,
                    timestamp DATETIME NOT NULL,
                    FOREIGN KEY (ID_post) REFERENCES Post(ID_post),
					FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario));
                    
/Tabla de foto de usuario/
CREATE TABLE Foto_usuario (ID_foto INT PRIMARY KEY auto_increment,
						   ID_usuario INT,
                           ubicacion VARCHAR (255),
                           FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario));
/usuarios/
              INSERT INTO Usuario (nombre_usuario, nombre, apellido, email, contrasena, fdenacimiento, telefono, sexo)
              VALUES
              ('@SofiDuarte','Sofia','Duarte','sofiianpablo@gmail.com','123123','1997-06-27','3624037657','F'),
              ('@escalantecamila','Camila','Escalante','escalantecamila.n@gmail.com','12345678','1997-10-09','3624094067','F'),
              ('@sbelbey','Saul','Belbey','saul@gmail.con','qwerty123','1988-09-12','3624599978','M'),
              ('@anika22sc','Ana','Santa Cruz','anacesiasantacruz@gmail.com','123456','2001-12-30','3624934986','F'),
              ('@barbievalentina','Barbie','Zaracho','barbarazaracho14@gmail.com','barbara99','2003-10-29','3624138011','F'),
              ('@joaaa23','Joaquin','Margoza','joaquinmargoza15@gmail.com','8966','2003-05-21','3624638752','M'),
              ('@Galfred','Jose Alfredo','Gay','Jose.Jose0011@hotmail.com','112200','1995-07-17','3625291081','M'),
              ('@esorellana','Esteban','Orellana','orellanaestebansalvador@gmail.com','9000','2002-01-12','3624132318','M'),
              ('@Facu15','Facundo','Escalante','escalnanfacundo@gmail.com','facu1509','2001-09-15','3624058720','M'),
              ('@Santi27','Santiago','Llano','slsanti31@gmail.com','727890Run','1999-09-27','3624947215','M'),
              ('@tomijp','Tomas','Pariggi','tomipariggi2004@gmail.com','2525','2004-01-07','3624165883','M')