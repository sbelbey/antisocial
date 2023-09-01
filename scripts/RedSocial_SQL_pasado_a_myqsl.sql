-- CREATE DATABASE RedSocial;
/* Tabla usuario*/
CREATE TABLE Usuario (ID_usuario INT PRIMARY KEY,
					  nombre VARCHAR(100) NOT NULL,
                      apellido VARCHAR (100) NOT NULL,
                      email VARCHAR(100) NOT NULL,
                      contrasena VARCHAR(15) NOT NULL,
                      fdenacimiento DATE,
                      telefono INT,
                      sexo BOOL);

/* Tabla Publicaciones*/ 
CREATE TABLE Post (ID_post INT PRIMARY KEY NOT NULL,
				   ID_usuario INT NOT NULL,
                   contenido TINYTEXT NOT NULL,
                   timestamp DATETIME NOT NULL,
                   FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario));
	
/* Tabla Comentarios*/
CREATE TABLE Comentario (ID_comentario INT PRIMARY KEY,
						 ID_post INT,
                         ID_usuario INT,
                         contenido TINYTEXT NOT NULL,
                         timestamp DATETIME NOT NULL,
                         FOREIGN KEY (ID_post) REFERENCES Post(ID_post),
                         FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario));

/* Tabla de Likes */
CREATE TABLE Likes (ID_like INT  PRIMARY KEY,
					ID_post INT,
                    ID_usuario INT,
                    timestamp DATETIME NOT NULL,
                    FOREIGN KEY (ID_post) REFERENCES Post(ID_post),
					FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario));
                    
/*Tabla de foto de usuario*/
CREATE TABLE Foto_usuario (ID_foto INT PRIMARY KEY,
						   ID_usuario INT,
                           ubicacion VARCHAR (255),
                           FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario));