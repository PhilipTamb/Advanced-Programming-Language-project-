package main

import (
	"database/sql"
	"fmt"
)

var sqlDB *sql.DB

func main() {

	//DB
	sqlDB = startDB()

	fmt.Println("E' il primo avvio del database? Se sì e hai bisogno di creare le tabelle inserisci 1 \n" +
		"Altrimenti, inserisci qualsiasi altro tasto per continuare e avviare il server: ")
	var answer string
	fmt.Scanf("%s", &answer)
	strYes := "1"
	if answer == strYes {
		databaseSetup(sqlDB)
	}
	esempioQuery(sqlDB)

	// server
	startServer()

}
