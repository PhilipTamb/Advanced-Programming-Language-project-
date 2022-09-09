package main

import (
	"database/sql"
	"fmt"
)

func databaseSetup(datab *sql.DB) {
	query1 := fmt.Sprintf("create table utenti(\n    id_utente integer(5) NOT NULL AUTO_INCREMENT,\n    nome VARCHAR(20),\n    cognome VARCHAR(20),\n    citta VARCHAR(20),\n    indirizzo VARCHAR(50),\n    PRIMARY KEY(id_utente)\n);")
	result1, error1 := datab.Query(query1)
	if error1 != nil {
		fmt.Println(error1)
	} else {
		defer result1.Close()
	}


	query2 := fmt.Sprintf("create table professionisti(\n    id_professionista integer(5) NOT NULL AUTO_INCREMENT,\n    nome VARCHAR(20),\n    cognome VARCHAR(20),\n    professione VARCHAR(50),\n    partita_iva VARCHAR(30),\n    recensione DECIMAL(2,1) DEFAULT 0.0,\n    citta VARCHAR(20),\n    indirizzo VARCHAR(50),\n    PRIMARY KEY(id_professionista)\n);")
	result2, error2 := datab.Query(query2)
	if error2 != nil {
		fmt.Println(error2)
	} else {
		defer result2.Close()
	}


	query3 := fmt.Sprintf("create table credenziali(\n    id_credenziale integer(5) NOT NULL AUTO_INCREMENT,\n    id_utente integer(5),\n    id_professionista integer(5),\n    email VARCHAR(50),\n    telefono varchar(13),\n    psw VARCHAR(30),\n    PRIMARY KEY(id_credenziale),\n    FOREIGN KEY (id_utente) REFERENCES utenti (id_utente),\n    FOREIGN KEY (id_professionista) REFERENCES professionisti (id_professionista)\n);")
	result3, error3 := datab.Query(query3)
	if error3 != nil {
		fmt.Println(error3)
	}
	defer result3.Close()

	query4 := fmt.Sprintf("create table tickets(\n    id_ticket integer(5) NOT NULL AUTO_INCREMENT,\n    id_utente integer(5),\n    id_professionista integer(5),\n    stato VARCHAR(10),\n    categoria VARCHAR(40),\n    titolo VARCHAR(50),\n    descrizione text,\n    PRIMARY KEY(id_ticket),\n    FOREIGN KEY (id_professionista) REFERENCES professionisti(id_professionista),\n    FOREIGN KEY (id_utente) REFERENCES utenti(id_utente)\n);")
	result4, error4 := datab.Query(query4)
	if error4 != nil {
		fmt.Println(error4)
	} else {
		defer result4.Close()
	}


	query5 := fmt.Sprintf("create table preventivi(\n    id_preventivo integer(5) NOT NULL AUTO_INCREMENT,\n    id_ticket integer(5),\n    id_professionista integer (5),\n    descrizione_intervento text,\n    materiali_o_ricambi_previsti text,\n    costo FLOAT(8,2),\n    dataora_intervento VARCHAR(20),\n    PRIMARY KEY (id_preventivo),\n    FOREIGN KEY (id_ticket) REFERENCES tickets (id_ticket),\n    FOREIGN KEY (id_professionista) REFERENCES professionisti(id_professionista)\n);")
	result5, error5 := datab.Query(query5)
	if error5 != nil {
		fmt.Println(error5)
	} else {
		defer result5.Close()
	}


	query6 := fmt.Sprintf("create table fatture(\n\tid_fattura integer(5) NOT NULL AUTO_INCREMENT,\n\tid_ticket integer(5),\n\tid_professionista integer (5),\n\tpath_fattura text,\n\tPRIMARY KEY (id_fattura),\n\tFOREIGN KEY (id_ticket) REFERENCES tickets (id_ticket),\n      FOREIGN KEY (id_professionista) REFERENCES professionisti(id_professionista)\n);")
	result6, error6 := datab.Query(query6)
	if error6 != nil {
		fmt.Println(error6)
	} else {
		defer result6.Close()
	}

}
