package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

func startServer() {
	fmt.Println("Start Server")
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
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func login(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()

	email := req.Form.Get("email")
	passw := req.Form.Get("password")
	print("SM " + email + " " + passw)
	fmt.Println(email + " " + passw)
	resp := loginQuery(sqlDB, email, passw)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)

}

func newticket(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	title := req.Form.Get("titolo")
	category := req.Form.Get("categoria")
	description := req.Form.Get("descrizione")
	email := req.Form.Get("email")
	resp := newticketQuery(sqlDB, title, category, description, email)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func getnome(w http.ResponseWriter, req *http.Request) {
	print("getnome")
	req.ParseForm()
	mail := req.Form.Get("email")
	print("\n getnome mail" + mail)
	resp := getnomeQuery(sqlDB, mail)
	fmt.Println("resp " + resp)
	fmt.Fprintf(w, resp)
}

func getickets(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	mail := req.Form.Get("email")
	resp := getTickets(sqlDB, mail)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func getprofessionisti(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	categoria := req.Form.Get("categoria")
	resp := getProfessionistiQuery(sqlDB, categoria)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func selectprofessionista(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	mail := req.Form.Get("email")
	idProfessionist := req.Form.Get("idProfessionista")
	resp := selectProfessionistaQuery(sqlDB, mail, idProfessionist)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func getpreventivi(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	mail := req.Form.Get("email")
	resp := getPreventiviQuery(sqlDB, mail)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func getinfopreventivo(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := getInfoPreventivoQuery(sqlDB, id)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func acceptpreventivo(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := acceptPreventivoQuery(sqlDB, id)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func denypreventivo(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	id := req.Form.Get("id")
	resp := denyPreventivoQuery(sqlDB, id)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func downloadfattura(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	email := req.Form.Get("mail")
	id_ticket := req.Form.Get("id_ticket")
	resp := downloadFatturaQuery(sqlDB, email, id_ticket)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func getprofessionistidavotare(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	mail := req.Form.Get("email")
	resp := getProfessionistiDaVotareQuery(sqlDB, mail)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func voteprofessionista(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	email := req.Form.Get("mail")
	id_ticket := req.Form.Get("id_ticket")
	voto := req.Form.Get("voto")
	id_professionista := req.Form.Get("id_professionista")
	resp := voteProfessionistaQuery(sqlDB, email, id_ticket, voto, id_professionista)
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func register_professionist(w http.ResponseWriter, req *http.Request) {
	fmt.Println("register_professionist")
	req.ParseForm()

	b, err := io.ReadAll(req.Body)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(string(b))

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
	fmt.Println(resp)
	fmt.Fprintf(w, resp)
}

func getnomeprofessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	mail := req.Form.Get("email")
	resp := getnomeprofessionistQuery(sqlDB, mail)
	fmt.Println("resp " + resp)
	fmt.Fprintf(w, resp)
}

func geticketsprofessionist(w http.ResponseWriter, req *http.Request) {
	print("geticketsprofessionist\n")
	req.ParseForm()
	mail := req.Form.Get("email")
	resp := getTicketsProfessionistQuery(sqlDB, mail)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func geticketsprofessionistbyid(w http.ResponseWriter, req *http.Request) {
	print("geticketsprofessionistbyid\n")
	req.ParseForm()
	mail := req.Form.Get("email")
	idTicket := req.Form.Get("idTicket")
	resp := getTicketsProfessionistByIdQuery(sqlDB, mail, idTicket)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func insertpreventivoprofessionist(w http.ResponseWriter, req *http.Request) {
	print("insertpreventivoprofessionist\n")
	req.ParseForm()
	mail := req.Form.Get("email")
	id_ticket := req.Form.Get("id_ticket")
	descrizione_intervento := req.Form.Get("descrizione_intervento")
	materiali_o_ricambi_previsti := req.Form.Get("materiali_o_ricambi_previsti")
	costo := req.Form.Get("costo")
	dataora_intervento := req.Form.Get("dataora_intervento")
	resp := InsertPreventivoProfessionistQuery(sqlDB, mail, id_ticket, descrizione_intervento, materiali_o_ricambi_previsti, costo, dataora_intervento)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func getpreventiviinattesaprofessionist(w http.ResponseWriter, req *http.Request) {
	req.ParseForm()
	mail := req.Form.Get("email")
	resp := getPreventiviInAttesaProfessionistQuery(sqlDB, mail)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func getpreventivoprofessionistbyidticket(w http.ResponseWriter, req *http.Request) {
	print("getpreventivoprofessionistbyidticket\n")
	req.ParseForm()
	mail := req.Form.Get("email")
	idTicket := req.Form.Get("idTicket")
	resp := getPreventiviProfessionistByIdTicketQuery(sqlDB, mail, idTicket)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func insertFatturaProfessionist(w http.ResponseWriter, req *http.Request) {
	print("insertFatturaProfessionist\n")
	req.ParseForm()
	id_ticket := req.Form.Get("id_ticket")
	id_preventivo := req.Form.Get("id_preventivo")
	id_professionista := req.Form.Get("id_professionista")
	path := req.Form.Get("path")
	mail := req.Form.Get("email")
	resp := insertFatturaProfessionistQuery(sqlDB, mail, id_ticket, id_preventivo, id_professionista, path)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}

func updatecostoProfessionist(w http.ResponseWriter, req *http.Request) {
	print("insertFatturaProfessionist\n")
	req.ParseForm()
	id_ticket := req.Form.Get("id_ticket")
	id_preventivo := req.Form.Get("id_preventivo")
	id_professionista := req.Form.Get("id_professionista")
	costo := req.Form.Get("path")
	mail := req.Form.Get("email")

	resp := updateCostoProfessionistQuery(sqlDB, mail, id_ticket, id_preventivo, id_professionista, costo)
	fmt.Println(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(resp)
}
