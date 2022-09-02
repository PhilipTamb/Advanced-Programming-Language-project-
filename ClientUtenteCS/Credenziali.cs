namespace ClientUtenteCS
{
    internal class Credenziali
    {
        public string Email { get; set; }
        public string Telefono { get; set; }
        public string Password { get; set; }

        public Credenziali(string email, string cellulare, string psw)
        {
            Email = email;
            Telefono = cellulare;
            Password = psw;
            
        }

    }
}
