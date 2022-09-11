package main

import (
	"database/sql"
	"fmt"
	"log"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
)

// classi presenti nel DB
type Utente struct {
	Id        int
	Nome      string
	Cognome   string
	Citta     string
	Indirizzo string
}

// i nomi dei campi degli struct sono indicati con la lettera iniziale maiuscola per alcuni problemi
// derivati dall'incapsulamento dello struct stesso in json
type Ticket struct {
	Id          int    //  `json:"id"`
	Stato       string //  `json:"stato"`
	Categoria   string //  `json:"categoria"`
	Titolo      string //  `json:"titolo"`
	Descrizione string //  `json:"descrizone"`
}
type Professionisti struct {
	Id          int
	Nome        string
	Cognome     string
	Professione string
	Recensione  float32
	Citta       string
}
type Preventivi struct {
	Id               int
	IdTicket         int
	IdProfessionista int
	Descrizione      string
	MaterialiRicambi string
	Costo            float32
	DataOra          string
}

func startDB() *sql.DB { //SPECIFICO LA PSW
	db, err := sql.Open("mysql", "root:root@tcp(localhost:3306)/instafix")
	//defer db.Close()

	if err != nil {
		log.Fatal(err)
	}

	var version string

	err2 := db.QueryRow("SELECT VERSION()").Scan(&version)

	if err2 != nil {
		log.Fatal(err2)
	}

	fmt.Println(version)
	fmt.Println("DB avviato")
	return db
}

func esempioQuery(datab *sql.DB) {
	res, err := datab.Query("SELECT * FROM utenti")

	defer res.Close()

	if err != nil {
		fmt.Println(err)
	}

	for res.Next() {

		var utente Utente
		err := res.Scan(&utente.Id, &utente.Nome, &utente.Cognome, &utente.Citta, &utente.Indirizzo)

		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("%v\n", utente)
	}

}

func registerQuery(datab *sql.DB, name string, surname string, city string, address string, email string, number string, passw string) string {
	res1, err1 := datab.Query("SELECT * FROM credenziali WHERE email=" + "'" + email + "'")
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	if res1.Next() == true {
		return "Email esistente"
	}
	defer res1.Close()

	query1 := fmt.Sprintf("INSERT INTO utenti (nome, cognome, citta, indirizzo) VALUES ('%s', '%s', '%s', '%s' )",
		name, surname, city, address)
	res2, err2 := datab.Query(query1)

	query2 := fmt.Sprintf("INSERT INTO credenziali (email, id_utente, psw, telefono) VALUES"+
		"('%s', (SELECT id_utente FROM utenti WHERE nome='%s' AND cognome='%s' AND indirizzo='%s'),"+
		" '%s', '%s')", email, name, surname, address, passw, number)
	res3, err3 := datab.Query(query2)

	if err2 != nil || err3 != nil {
		fmt.Println(err2)
		fmt.Println(err3)
		return "Errore generico"
	}
	defer res2.Close()
	defer res3.Close()
	return "Account creato"

}

func loginQuery(datab *sql.DB, email string, psw string) string {
	fmt.Println("DB" + email + " " + psw)
	query := fmt.Sprintf("SELECT email FROM credenziali WHERE email= '%s' AND psw='%s'", email, psw)
	result1, err1 := datab.Query(query)

	if result1.Next() == false {
		return "Credenziali errate"
	}
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	defer result1.Close()

	return "Credenziali corrette"

}

func newticketQuery(datab *sql.DB, title string, category string, desc string, email string) string {
	query1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente="+
		"(SELECT id_utente FROM credenziali WHERE email='%s')", email)
	res1, err1 := datab.Query(query1)
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	defer res1.Close()
	var idUser int
	// estrapoliamo l'id utente trovato nella query precedente per poterlo utilizzare nella query successiva
	for res1.Next() {
		err := res1.Scan(&idUser)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(idUser)
	}

	if idUser > 0 {
		query2 := fmt.Sprintf("INSERT INTO tickets (id_utente, categoria, titolo, descrizione, stato)"+
			"VALUES ('%d', '%s', '%s', '%s', 'creato')", idUser, category, title, desc)
		result, err := datab.Query(query2)
		if err != nil {
			fmt.Println(err)
			return "Errore generico"
		}
		defer result.Close()
		return "Ticket creato"
	}
	return "Utente non trovato"
}

func getnomeQuery(datab *sql.DB, mail string) string {
	print("\n getNomeQuery")
	print("\n mail " + mail)
	query := fmt.Sprintf("SELECT nome FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	res, err := datab.Query(query)
	fmt.Println(query)
	fmt.Println(res)

	if err != nil {
		fmt.Println(err)
		return "Errore generico"
	}
	defer res.Close()

	var nome string
	for res.Next() {
		err2 := res.Scan(&nome)
		if err2 != nil {
			log.Fatal(err2)
		}
	}
	return nome
}

func getTickets(datab *sql.DB, mail string) []Ticket {
	q1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	r1, err1 := datab.Query(q1)
	if err1 != nil {
		fmt.Println(err1)
	} else {
		defer r1.Close()
	}

	var id int
	for r1.Next() {
		err2 := r1.Scan(&id)
		if err2 != nil {
			log.Fatal(err2)
		}
	}
	q2 := fmt.Sprintf("SELECT id_ticket, stato, categoria, titolo, descrizione FROM tickets WHERE "+
		"id_utente='%d'", id)
	r2, err3 := datab.Query(q2)

	if err3 != nil {
		fmt.Println(err3)
	} else {
		defer r2.Close()
	}

	var richiesta Ticket
	var tickets []Ticket
	// abbiamo bisogno di un array perchè un utente potrebbe avere più ticket creati alla volta
	for r2.Next() {
		err4 := r2.Scan(&richiesta.Id, &richiesta.Stato, &richiesta.Categoria, &richiesta.Titolo, &richiesta.Descrizione)
		if err4 != nil {
			log.Fatal(err4)
		}
		tickets = append(tickets, richiesta)
	}

	return tickets
}

func getProfessionistiQuery(datab *sql.DB, category string) []Professionisti {
	query := fmt.Sprintf("SELECT id_professionista, nome, cognome, professione, recensione, citta FROM professionisti"+
		" WHERE professione='%s' ORDER BY recensione DESC", category)
	resp, err := datab.Query(query)
	if err != nil {
		fmt.Println(err)
	} else {
		defer resp.Close()
	}

	var lavoratore Professionisti
	var professionisti []Professionisti
	for resp.Next() {
		err2 := resp.Scan(&lavoratore.Id, &lavoratore.Nome, &lavoratore.Cognome, &lavoratore.Professione,
			&lavoratore.Recensione, &lavoratore.Citta)
		if err2 != nil {
			log.Fatal(err2)
		}

		professionisti = append(professionisti, lavoratore)
	}
	return professionisti
}

func selectProfessionistaQuery(datab *sql.DB, mail string, id_professionist string) string {
	query1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	res1, err1 := datab.Query(query1)
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	defer res1.Close()
	var idUser int
	for res1.Next() {
		err2 := res1.Scan(&idUser)
		if err2 != nil {
			log.Fatal(err2)
		}
	}
	idProfessionist, err := strconv.Atoi(id_professionist)
	if err != nil {
		// ... handle error
		fmt.Println(err)
	}

	// aggiorna il ticket inserendo l'id del professionista scelto dall'utente
	// viene sempre preso il ticket dell'utente con l'id maggiore in quanto è l'ultimo creato dall'utente
	query2 := fmt.Sprintf("UPDATE tickets SET id_professionista=%d WHERE"+
		" id_ticket= (SELECT MAX(id_ticket) FROM tickets WHERE id_utente=%d)", idProfessionist, idUser)
	resUpdate, errUpdate := datab.Query(query2)
	if errUpdate != nil {
		fmt.Println(errUpdate)
		return "Errore generico"
	}
	defer resUpdate.Close()
	return "ok"
}

func getPreventiviQuery(datab *sql.DB, mail string) []Preventivi {
	q1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	r1, err1 := datab.Query(q1)
	if err1 != nil {
		fmt.Println(err1)
	} else {
		defer r1.Close()
	}

	var idUser int
	for r1.Next() {
		err2 := r1.Scan(&idUser)
		if err2 != nil {
			log.Fatal(err2)
		}
	}

	q2 := fmt.Sprintf("SELECT * FROM preventivi WHERE id_ticket IN (SELECT id_ticket FROM tickets WHERE "+
		"id_utente= %d AND stato='in attesa')", idUser)
	r2, err3 := datab.Query(q2)
	if err3 != nil {
		fmt.Println(err3)
	} else {
		defer r2.Close()
	}

	var preventivo Preventivi
	var listaPreventivi []Preventivi

	for r2.Next() {
		err4 := r2.Scan(&preventivo.Id, &preventivo.IdTicket, &preventivo.IdProfessionista, &preventivo.Descrizione, &preventivo.MaterialiRicambi, &preventivo.Costo, &preventivo.DataOra)
		if err4 != nil {
			log.Fatal(err4)
		}
		listaPreventivi = append(listaPreventivi, preventivo)
	}

	return listaPreventivi
}

func getInfoPreventivoQuery(datab *sql.DB, id string) Preventivi {
	idPreventivo, err1 := strconv.Atoi(id)
	if err1 != nil {
		fmt.Println(err1)
	}

	query := fmt.Sprintf("SELECT * FROM preventivi WHERE id_preventivo= %d", idPreventivo)
	response, errore := datab.Query(query)

	if errore != nil {
		fmt.Println(errore)
	} else {
		defer response.Close()
	}

	var infoPreventivo Preventivi

	for response.Next() {
		err := response.Scan(&infoPreventivo.Id, &infoPreventivo.IdTicket, &infoPreventivo.IdProfessionista, &infoPreventivo.Descrizione, &infoPreventivo.MaterialiRicambi, &infoPreventivo.Costo, &infoPreventivo.DataOra)
		if err != nil {
			log.Fatal(err)
		}
	}

	return infoPreventivo
}

func acceptPreventivoQuery(datab *sql.DB, id string) string {
	idPreventivo, err1 := strconv.Atoi(id)
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}

	query := fmt.Sprintf("UPDATE TICKETS set stato='in corso' WHERE id_ticket= (SELECT id_ticket FROM"+
		" preventivi WHERE id_preventivo= %d)", idPreventivo)

	response, errore := datab.Query(query)

	if errore != nil {
		fmt.Println(errore)
		return "Errore generico"
	}
	defer response.Close()

	return "Preventivo accettato"
}

func denyPreventivoQuery(datab *sql.DB, id string) string {
	idPreventivo, err1 := strconv.Atoi(id)
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}

	query := fmt.Sprintf("UPDATE TICKETS set stato='rifiutato' WHERE id_ticket= (SELECT id_ticket FROM"+
		" preventivi WHERE id_preventivo= %d)", idPreventivo)

	response, errore := datab.Query(query)

	if errore != nil {
		fmt.Println(errore)
		return "Errore generico"
	}
	defer response.Close()

	return "Preventivo rifiutato"
}

func downloadFatturaQuery(datab *sql.DB, mail string, id_ticket string) string {
	idTicket, errr := strconv.Atoi(id_ticket)
	if errr != nil {
		fmt.Println(errr)
		return "Errore generico"
	}

	q1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	r1, err1 := datab.Query(q1)
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	defer r1.Close()
	var idUser int
	for r1.Next() {
		err2 := r1.Scan(&idUser)
		if err2 != nil {
			fmt.Println(err2)
			return "Errore generico"
		}
	}
	// si controlla se la fattura che l'utente vuole scaricare si riferisce a un ticket aperto da lui
	// e anche se il ticket è stato completato (stato finito)
	q2 := fmt.Sprintf("SELECT path_fattura FROM fatture WHERE id_ticket= (SELECT id_ticket FROM tickets"+
		" WHERE id_ticket= %d AND id_utente= %d AND stato='finito')", idTicket, idUser)
	r2, err2 := datab.Query(q2)
	if err2 != nil {
		fmt.Println(err2)
		return "Errore generico"
	}
	defer r2.Close()
	var pathFile string
	for r2.Next() {
		err3 := r2.Scan(&pathFile)
		if err3 != nil {
			fmt.Println(err3)
			return "Errore generico"
		}
	}

	if pathFile == "" {
		return "Non disponibile"
	}

	// le fatture vengono salvate nella directory "fatture" del server locale
	// ES http://localhost/fatture/fatt_31.pdf

	return pathFile
}

func getProfessionistiDaVotareQuery(datab *sql.DB, mail string) []Professionisti {
	q1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	r1, err1 := datab.Query(q1)
	if err1 != nil {
		fmt.Println(err1)
	} else {
		defer r1.Close()
	}

	var idUser int
	for r1.Next() {
		err2 := r1.Scan(&idUser)
		if err2 != nil {
			log.Fatal(err2)
		}
	}

	q2 := fmt.Sprintf("SELECT id_professionista, nome, cognome, professione, recensione, citta"+
		" FROM professionisti WHERE id_professionista IN (SELECT id_professionista FROM"+
		" tickets WHERE id_utente= %d AND stato='finito')", idUser)
	r2, err2 := datab.Query(q2)
	if err2 != nil {
		fmt.Println(err2)
	} else {
		defer r2.Close()
	}

	var lavoratore Professionisti
	var professionisti []Professionisti
	for r2.Next() {
		err3 := r2.Scan(&lavoratore.Id, &lavoratore.Nome, &lavoratore.Cognome, &lavoratore.Professione,
			&lavoratore.Recensione, &lavoratore.Citta)
		if err3 != nil {
			log.Fatal(err3)
		}

		professionisti = append(professionisti, lavoratore)
	}
	return professionisti

}

func voteProfessionistaQuery(datab *sql.DB, mail string, id_ticket string, voto string, id_professionista string) string {
	idTicket, err1 := strconv.Atoi(id_ticket)
	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	valutazione, err2 := strconv.Atoi(voto)
	if err2 != nil {
		fmt.Println(err2)
		return "Errore generico"
	}

	idProfessionista, errore := strconv.Atoi(id_professionista)
	if errore != nil {
		fmt.Println(errore)
		return "Errore generico"
	}

	q1 := fmt.Sprintf("SELECT id_utente FROM utenti WHERE id_utente=(SELECT id_utente FROM credenziali "+
		"WHERE email='%s')", mail)
	r1, err3 := datab.Query(q1)
	if err3 != nil {
		fmt.Println(err3)
		return "Errore generico"
	}
	defer r1.Close()
	var idUser int
	for r1.Next() {
		err4 := r1.Scan(&idUser)
		if err4 != nil {
			fmt.Println(err4)
			return "Errore generico"
		}
	}
	// controllo del numero del ticket inserito dall'utente, per vedere se corrisponde a quel determinato
	// utente e a quel professionista da lui selezionato
	q2 := fmt.Sprintf("SELECT id_ticket FROM tickets WHERE id_ticket= %d AND id_utente= %d AND"+
		" id_professionista= %d AND stato='finito'", idTicket, idUser, idProfessionista)
	r2, err5 := datab.Query(q2)
	if err5 != nil {
		fmt.Println(err5)
		return "Errore generico"
	}
	defer r2.Close()
	var checkIdTicket int
	for r2.Next() {
		err6 := r2.Scan(&checkIdTicket)
		if err6 != nil {
			fmt.Println(err6)
			return "Errore generico"
		}
	}

	if checkIdTicket > 0 {
		q3 := fmt.Sprintf("SELECT recensione FROM professionisti WHERE id_professionista= %d", idProfessionista)
		r3, err7 := datab.Query(q3)
		if err7 != nil {
			fmt.Println(err7)
			return "Errore generico"
		}
		defer r3.Close()
		var actualReview float64
		for r3.Next() {
			err8 := r3.Scan(&actualReview)
			if err8 != nil {
				fmt.Println(err8)
				return "Errore generico"
			}
		}

		// aggiornamento della media del voto del professionista
		var newReview float64
		if actualReview <= 0 {
			newReview = float64(valutazione)
		} else {
			newReview = (actualReview + float64(valutazione)) / 2
		}

		q4 := fmt.Sprintf("UPDATE professionisti SET recensione= %f WHERE id_professionista= %d",
			newReview, idProfessionista)
		r4, err9 := datab.Query(q4)
		if err9 != nil {
			fmt.Println(err9)
			return "Errore generico"
		}
		defer r4.Close()

		// aggiornamento dello stato del ticket per evitare che l'utente possa votare più volte
		q5 := fmt.Sprintf("UPDATE tickets SET stato='votato' WHERE id_ticket= %d", idTicket)
		r5, err10 := datab.Query(q5)
		if err10 != nil {
			fmt.Println(err10)
			return "Errore generico"
		}
		defer r5.Close()

		return "Voto aggiunto"
	}

	return "Check fallito"

}

func registerQueryProfessionist(datab *sql.DB, name string, surname string, professione string, partitaiva string, city string, address string, email string, number string, passw string) string {
	fmt.Println("registerQueryProfessionist")
	//SELECT * FROM `credenziali` WHERE 1
	res1, err1 := datab.Query("SELECT * FROM credenziali WHERE email=" + "'" + email + "' LIMIT 1")
	defer res1.Close()
	if err1 != nil {
		fmt.Println("Error in query credenziali")
		log.Fatal(err1)
	}
	if res1.Next() == true {
		return "Email esistente"
	}

	for res1.Next() {
		var id_credenziale string
		var id_utente string
		var id_professionista string
		var email string
		var telefono string
		var psw string
		err1 = res1.Scan(&id_credenziale, &id_utente, &id_professionista, &email, &telefono, &psw)
	}

	//INSERT INTO `professionisti` (`id_professionista`, `nome`, `cognome`, `professione`, `partita_iva`, `recensione`, `citta`, `indirizzo`)
	query1 := fmt.Sprintf("INSERT INTO professionisti (nome, cognome, professione, partita_iva, citta, indirizzo) VALUES ('%s', '%s', '%s', '%s','%s', '%s')",
		name, surname, professione, partitaiva, city, address)

	res2, err2 := datab.Query(query1)
	defer res2.Close()
	if err2 != nil {
		log.Fatal(err2)
		return "Errore generico"
	}

	query3 := fmt.Sprintf("SELECT id_professionista FROM professionisti WHERE partita_iva = '%s' AND nome='%s' AND cognome='%s' LIMIT 1", partitaiva, name, surname)

	res4, err4 := datab.Query(query3)
	defer res4.Close()
	if err4 != nil {
		log.Fatal(err4)
		log.Fatal(err4)
		return "Errore generico"
	}

	for res4.Next() {
		var id_professionista string
		err1 = res1.Scan(&id_professionista)
	}

	query2 := fmt.Sprintf("INSERT INTO credenziali (email, id_professionista, psw, telefono) VALUES"+
		"('%s', (SELECT id_professionista FROM professionisti WHERE partita_iva = '%s' AND nome='%s' AND cognome='%s' LIMIT 1),"+
		" '%s', '%s')", email, partitaiva, name, surname, passw, number)

	//query2 := fmt.Sprintf("INSERT INTO credenziali (id_credenziale, id_utente, id_professionista, email, telefono, psw) VALUES ('2', '1', '2', '@', '331', 'psw')")

	res3, err3 := datab.Query(query2)
	defer res3.Close()
	if err3 != nil {
		log.Fatal(err3)
		return "Errore generico"
	}

	return "Account creato"

}

func getnomeprofessionistQuery(datab *sql.DB, id_professionista string) string {
	query := fmt.Sprintf("SELECT nome FROM professionisti WHERE id_professionista='%s' ", id_professionista)
	res, err := datab.Query(query)

	if err != nil {
		fmt.Println(err)
		return "Errore generico"
	}
	defer res.Close()

	var nome string
	for res.Next() {
		err2 := res.Scan(&nome)
		if err2 != nil {
			log.Fatal(err2)
		}
	}
	return nome
}

func getTicketsProfessionistQuery(datab *sql.DB, id_professionista string) []Ticket {
	print("getTicketsProfessionistQuery\n")
	q2 := fmt.Sprintf("SELECT id_ticket, stato, categoria, titolo, descrizione FROM tickets WHERE id_professionista='%s'", id_professionista)
	r2, err3 := datab.Query(q2)

	if err3 != nil {
		fmt.Println(err3)
	} else {
		defer r2.Close()
	}

	var richiesta Ticket
	var tickets []Ticket
	// abbiamo bisogno di un array perchè un utente potrebbe avere più ticket creati alla volta
	for r2.Next() {
		err4 := r2.Scan(&richiesta.Id, &richiesta.Stato, &richiesta.Categoria, &richiesta.Titolo, &richiesta.Descrizione)
		if err4 != nil {
			log.Fatal(err4)
		}

		tickets = append(tickets, richiesta)
	}

	return tickets
}

func getTicketsProfessionistByIdQuery(datab *sql.DB, id_professionista string, id_ticket string) []Ticket {
	print("getTicketsProfessionistByIdQuery\n")
	q2 := fmt.Sprintf("SELECT id_ticket, stato, categoria, titolo, descrizione FROM tickets WHERE "+
		"id_professionista='%s' AND id_ticket='%s' ", id_professionista, id_ticket)
	r2, err3 := datab.Query(q2)

	fmt.Println(q2)

	fmt.Println(r2)

	if err3 != nil {
		fmt.Println(err3)
	} else {
		defer r2.Close()
	}

	var richiesta Ticket
	var tickets []Ticket
	// abbiamo bisogno di un array perchè un utente potrebbe avere più ticket creati alla volta
	for r2.Next() {
		err4 := r2.Scan(&richiesta.Id, &richiesta.Stato, &richiesta.Categoria, &richiesta.Titolo, &richiesta.Descrizione)
		if err4 != nil {
			log.Fatal(err4)
		}
		fmt.Println(tickets)
		fmt.Println(richiesta)
		tickets = append(tickets, richiesta)
	}

	return tickets
}

func InsertPreventivoProfessionistQuery(datab *sql.DB, id_professionista string, id_ticket string, descrizione_intervento string, materiali_o_ricambi_previsti string, costo string, dataora_intervento string) string {
	print("InsertPreventivoProfessionistQuery\n")

	q2 := fmt.Sprintf("INSERT INTO preventivi (id_ticket, id_professionista, descrizione_intervento, materiali_o_ricambi_previsti, costo, dataora_intervento)"+
		" VALUES ('%s', '%s', '%s', '%s', '%s', '%s')", id_ticket, id_professionista, descrizione_intervento, materiali_o_ricambi_previsti, costo, dataora_intervento)
	fmt.Println(q2)
	r2, err3 := datab.Query(q2)

	if err3 != nil {
		fmt.Println(err3)
		return "Errore generico"
	} else {
		defer r2.Close()
	}

	query := fmt.Sprintf("UPDATE tickets set stato='in attesa' WHERE id_ticket= '%s'", id_ticket)

	response, errore := datab.Query(query)

	if errore != nil {
		fmt.Println(errore)
		return "Errore generico"
	}
	defer response.Close()

	return "Inserito correttamente"
}

// DA COMPLETARE
func getPreventiviInAttesaProfessionistQuery(datab *sql.DB, id_professionista string) []Preventivi {
	q2 := fmt.Sprintf("SELECT * FROM preventivi WHERE id_ticket IN (SELECT id_ticket FROM tickets WHERE "+
		"id_professionista = '%s' AND stato='in attesa' ) ", id_professionista) // AND stato='in attesa' il professionista visualizza i preventi
	r2, err3 := datab.Query(q2)
	if err3 != nil {
		fmt.Println(err3)
	} else {
		defer r2.Close()
	}

	var preventivo Preventivi
	var listaPreventivi []Preventivi

	for r2.Next() {
		err4 := r2.Scan(&preventivo.Id, &preventivo.IdTicket, &preventivo.IdProfessionista, &preventivo.Descrizione, &preventivo.MaterialiRicambi, &preventivo.Costo, &preventivo.DataOra)
		if err4 != nil {
			log.Fatal(err4)
		}
		listaPreventivi = append(listaPreventivi, preventivo)
	}

	return listaPreventivi
}

func getPreventiviProfessionistByIdTicketQuery(datab *sql.DB, id_professionista string, id_ticket string) []Preventivi {
	q2 := fmt.Sprintf("SELECT * FROM preventivi WHERE id_ticket = '%s' AND  id_professionista = '%s' ", id_ticket, id_professionista)
	r2, err3 := datab.Query(q2)
	if err3 != nil {
		fmt.Println(err3)
	} else {
		defer r2.Close()
	}
	var preventivo Preventivi
	var listaPreventivi []Preventivi

	for r2.Next() {
		err4 := r2.Scan(&preventivo.Id, &preventivo.IdTicket, &preventivo.IdProfessionista, &preventivo.Descrizione, &preventivo.MaterialiRicambi, &preventivo.Costo, &preventivo.DataOra)
		if err4 != nil {
			log.Fatal(err4)
		}
		listaPreventivi = append(listaPreventivi, preventivo)
	}

	return listaPreventivi
}

func insertFatturaProfessionistQuery(datab *sql.DB, id_ticket string, id_preventivo string, id_professionista string, path string) string {
	q2 := fmt.Sprintf("INSERT INTO fatture (id_ticket, id_professionista, path_fattura) VALUES ('%s', '%s', '%s')", id_ticket, id_professionista, path)
	fmt.Println(q2)
	r2, err3 := datab.Query(q2)

	fmt.Println(r2)

	if err3 != nil {
		fmt.Println(err3)
		return "Errore generico"
	} else {
		defer r2.Close()
	}

	query := fmt.Sprintf("UPDATE tickets set stato='finito' WHERE id_ticket= '%s'", id_ticket)

	response, errore := datab.Query(query)

	if errore != nil {
		fmt.Println(errore)
		return "Errore generico"
	}
	defer response.Close()

	return "Inserito correttamente"
}

func updateCostoProfessionistQuery(datab *sql.DB, id_ticket string, id_preventivo string, id_professionista string, costo string) string {
	print("getTicketsProfessionistByIdQuery\n")
	q2 := fmt.Sprintf("UPDATE preventivi SET costo = '%s' WHERE id_preventivo =  '%s' AND id_ticket = '%s' AND id_professionista = '%s' ", costo, id_preventivo, id_ticket, id_professionista)

	r2, err3 := datab.Query(q2)

	if err3 != nil {
		fmt.Println(err3)
		return "Errore generico"
	} else {
		defer r2.Close()
	}

	return "inserito correttamente"
}

func denyticketQuery(datab *sql.DB, id_ticket string) string {

	query := fmt.Sprintf("UPDATE tickets set stato='rifiutato' WHERE id_ticket= '%s'", id_ticket)

	response, errore := datab.Query(query)

	if errore != nil {
		fmt.Println(errore)
		return "Errore generico"
	}
	defer response.Close()

	return "Preventivo rifiutato"
}

func loginProfessionistQuery(datab *sql.DB, email string, psw string) string {
	fmt.Println("DB" + email + " " + psw)
	query := fmt.Sprintf("SELECT id_professionista FROM credenziali WHERE email= '%s' AND psw='%s'", email, psw)
	result1, err1 := datab.Query(query)

	if err1 != nil {
		fmt.Println(err1)
		return "Errore generico"
	}
	defer result1.Close()

	var idProf string
	for result1.Next() {
		err2 := result1.Scan(&idProf)
		if err2 != nil {
			log.Fatal(err2)
		}
	}

	if idProf == "" {
		return "Credenziali errate"
	}
	return idProf

}

func getRecensioneProfessionistQuery(datab *sql.DB, id_professionista string) string {
	print("\n getRecensioneProfessionistQuery")
	query := fmt.Sprintf(" SELECT recensione FROM professionisti WHERE id_professionista = '%s' ", id_professionista)
	res, err := datab.Query(query)
	fmt.Println(query)
	fmt.Println(res)

	if err != nil {
		fmt.Println(err)
		return "Errore generico"
	}
	defer res.Close()

	var recensione string
	for res.Next() {
		err2 := res.Scan(&recensione)
		if err2 != nil {
			log.Fatal(err2)
		}
	}
	return recensione
}
