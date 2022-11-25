package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func startServer() {
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/register", register)
	http.HandleFunc("/login", login)
	http.HandleFunc("/newticket", newticket)
	http.HandleFunc("/getnome", getnome)
	http.HandleFunc("/getickets", getickets)
	http.HandleFunc("/getprofessionisti", getprofessionisti)
	http.HandleFunc("/selectprofessionista", selectprofessionista)
	http.HandleFunc("/getpreventivi", getpreventivi)
	http.HandleFunc("/getinfopreventivo", getinfopreventivo)
	http.HandleFunc("/acceptpreventivo", acceptpreventivo)
	http.HandleFunc("/denypreventivo", denypreventivo)
	http.HandleFunc("/downloadfattura", downloadfattura)
	http.HandleFunc("/getprofessionistidavotare", getprofessionistidavotare)
	http.HandleFunc("/voteprofessionista", voteprofessionista)
	http.HandleFunc("/register_professionist", register_professionist)
	http.HandleFunc("/getnomeprofessionist", getnomeprofessionist)
	http.HandleFunc("/getpreventiviinattesaprofessionist", getpreventiviinattesaprofessionist)
	http.HandleFunc("/geticketsprofessionist", geticketsprofessionist)
	http.HandleFunc("/insertpreventivoprofessionist", insertpreventivoprofessionist)
	http.HandleFunc("/geticketsprofessionistbyid", geticketsprofessionistbyid)
	http.HandleFunc("/getpreventivoprofessionistbyidticket", getpreventivoprofessionistbyidticket)
	http.HandleFunc("/insertFatturaProfessionist", insertFatturaProfessionist)
	http.HandleFunc("/updatecostoProfessionist", updatecostoProfessionist)
	http.HandleFunc("/uploadfile", uploadfile)
	http.HandleFunc("/denyticket", denyticket)
	http.HandleFunc("/loginProfessionist", loginProfessionist)
	http.HandleFunc("/getrecensioneprofessionist", getrecensioneprofessionist)
	http.ListenAndServe(":8000", nil)

}

func hello(w http.ResponseWriter, req *http.Request) {

	fmt.Fprintf(w, "hello\n")
	fmt.Println("Hello path raggiunto")
}

// !!!!! funzione di prova
func headers(w http.ResponseWriter, req *http.Request) {

	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
	fmt.Println("Stampa degli headers")
}

// !!!!  funzione di prova
func upload(w http.ResponseWriter, req *http.Request) {
	b, err := io.ReadAll(req.Body)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(string(b))

}

func register(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	name := req.Form.Get("nome")
	surname := req.Form.Get("cognome")
	city := req.Form.Get("citta")
	address := req.Form.Get("indirizzo")
	email := req.Form.Get("email")
	number := req.Form.Get("telefono")
	passw := req.Form.Get("password")
	resp := registerQuery(sqlDB, name, surname, city, address, email, number, passw)
	fmt.Fprintf(w, resp)
}

func login(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	email := req.Form.Get("email")
	passw := req.Form.Get("password")
	resp := loginQuery(sqlDB, email, passw)
	fmt.Fprintf(w, resp)

}

func newticket(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	title := req.Form.Get("titolo")
	category := req.Form.Get("categoria")
	description := req.Form.Get("descrizione")
	id := req.Form.Get("id_utente")
	resp := newticketQuery(sqlDB, title, category, description, id)
	fmt.Fprintf(w, resp)
}

func getnome(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := getnomeQuery(sqlDB, id)
	fmt.Fprintf(w, resp)
}

func getickets(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id_utente")
	resp := getTickets(sqlDB, id)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)

}

func getprofessionisti(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	categoria := req.Form.Get("categoria")
	resp := getProfessionistiQuery(sqlDB, categoria)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func selectprofessionista(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	idUser := req.Form.Get("id_utente")
	idProfessionist := req.Form.Get("idProfessionista")
	resp := selectProfessionistaQuery(sqlDB, idUser, idProfessionist)
	fmt.Fprintf(w, resp)
}

func getpreventivi(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	idUser := req.Form.Get("id_utente")
	resp := getPreventiviQuery(sqlDB, idUser)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func getinfopreventivo(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := getInfoPreventivoQuery(sqlDB, id)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func acceptpreventivo(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := acceptPreventivoQuery(sqlDB, id)
	fmt.Fprintf(w, resp)
}

func denypreventivo(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := denyPreventivoQuery(sqlDB, id)
	fmt.Fprintf(w, resp)
}

func downloadfattura(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	idUser := req.Form.Get("id_utente")
	id_ticket := req.Form.Get("id_ticket")
	resp := downloadFatturaQuery(sqlDB, idUser, id_ticket)
	fmt.Fprintf(w, resp)
}

func getprofessionistidavotare(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	idUser := req.Form.Get("id_utente")
	resp := getProfessionistiDaVotareQuery(sqlDB, idUser)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func voteprofessionista(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	idUser := req.Form.Get("id_utente")
	id_ticket := req.Form.Get("id_ticket")
	voto := req.Form.Get("voto")
	id_professionista := req.Form.Get("id_professionista")
	resp := voteProfessionistaQuery(sqlDB, idUser, id_ticket, voto, id_professionista)
	fmt.Fprintf(w, resp)
}

func register_professionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	name := req.Form.Get("nome")
	surname := req.Form.Get("cognome")
	professione := req.Form.Get("professione")
	partitaiva := req.Form.Get("partitaiva")
	city := req.Form.Get("citta")
	address := req.Form.Get("indirizzo")
	email := req.Form.Get("email")
	number := req.Form.Get("telefono")
	passw := req.Form.Get("password")
	resp := registerQueryProfessionist(sqlDB, name, surname, professione, partitaiva, city, address, email, number, passw)
	fmt.Fprintf(w, resp)
}

func getnomeprofessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	resp := getnomeprofessionistQuery(sqlDB, id_professionista)
	fmt.Fprintf(w, resp)
}

func geticketsprofessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	resp := getTicketsProfessionistQuery(sqlDB, id_professionista)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func geticketsprofessionistbyid(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	id_ticket := req.Form.Get("id_ticket")
	resp := getTicketsProfessionistByIdQuery(sqlDB, id_professionista, id_ticket)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func insertpreventivoprofessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	id_ticket := req.Form.Get("id_ticket")
	descrizione_intervento := req.Form.Get("descrizione_intervento")
	materiali_o_ricambi_previsti := req.Form.Get("materiali_o_ricambi_previsti")
	costo := req.Form.Get("costo")
	dataora_intervento := req.Form.Get("dataora_intervento")
	resp := InsertPreventivoProfessionistQuery(sqlDB, id_professionista, id_ticket, descrizione_intervento, materiali_o_ricambi_previsti, costo, dataora_intervento)
	fmt.Fprintf(w, resp)
}

func getpreventiviinattesaprofessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	resp := getPreventiviInAttesaProfessionistQuery(sqlDB, id_professionista)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func getpreventivoprofessionistbyidticket(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	id_ticket := req.Form.Get("id_ticket")
	resp := getPreventiviProfessionistByIdTicketQuery(sqlDB, id_professionista, id_ticket)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func insertFatturaProfessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_ticket := req.Form.Get("id_ticket")
	id_preventivo := req.Form.Get("id_preventivo")
	id_professionista := req.Form.Get("id_professionista")
	path := req.Form.Get("path")
	resp := insertFatturaProfessionistQuery(sqlDB, id_ticket, id_preventivo, id_professionista, path)
	fmt.Fprintf(w, resp)
}

func updatecostoProfessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_ticket := req.Form.Get("id_ticket")
	id_preventivo := req.Form.Get("id_preventivo")
	id_professionista := req.Form.Get("id_professionista")
	costo := req.Form.Get("costo")
	resp := updateCostoProfessionistQuery(sqlDB, id_ticket, id_preventivo, id_professionista, costo)
	fmt.Fprintf(w, resp)

}

func uploadfile(w http.ResponseWriter, req *http.Request) {
	print("uploadfile")
	req.ParseMultipartForm(32 << 20) //32Mb
	file, handler, err := req.FormFile("file")
	if err != nil {
		print("\nError", err)
	}
	defer file.Close()

	// se si è LINUX utilizzare questo statement, ricordandosi di inserire tutti i file go nella cartella
	// del server (se si utilizza Apache è /var/www/html)
	// f, err := os.OpenFile("../fatture/"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)
	// se si è su Windows, inserire il path della cartella fatture in cui gira il server locale
	// (se si utilizza Apache la cartella è DISCO\xamp\htdosc)
	//z, err := os.OpenFile("C:\\xampp\\fatture\\"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)

	f, err := os.OpenFile("C:\\xampp\\htdocs\\fatture\\"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)

	if err != nil {
		print("\nError", err)
	}

	defer f.Close()

	io.Copy(f, file) //salvataggio file

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(handler.Filename)
}

func denyticket(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id_ticket := req.Form.Get("id_ticket")
	resp := denyticketQuery(sqlDB, id_ticket)
	fmt.Fprintf(w, resp)
}

func loginProfessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	email := req.Form.Get("email")
	passw := req.Form.Get("password")
	resp := loginProfessionistQuery(sqlDB, email, passw)
	fmt.Fprintf(w, resp)

}

func getrecensioneprofessionist(w http.ResponseWriter, req *http.Request) {
	print("getrecensioneprofessionist")
	req.ParseForm()
	id_professionista := req.Form.Get("id_professionista")
	resp := getRecensioneProfessionistQuery(sqlDB, id_professionista)
	fmt.Println("resp " + resp)
	fmt.Fprintf(w, resp)
}
