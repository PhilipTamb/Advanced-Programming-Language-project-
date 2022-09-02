
namespace ClientUtenteCS
{
    internal class Utente
    {
        public string Nome { get; set; }

        public string Cognome { get; set; }
        // public int Id;
        public string Citta { get; set; }
        public string Indirizzo { get; set; }
        
        public Credenziali Credenziali { get; set; }

        public Utente(string name, string surname, string city, string address, Credenziali cred)
        {
            Nome = name;
            Cognome = surname;
            Citta = city;
            Indirizzo = address;
            Credenziali = cred;
        }
    }
}
