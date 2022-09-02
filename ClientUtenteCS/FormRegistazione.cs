using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Diagnostics;
using System.Net.Http;
using System.Text.RegularExpressions; // per utilizzare Regex per controllo email e password

namespace ClientUtenteCS
{
    public partial class RegisterForm : Form
    {
        public RegisterForm()
        {
            InitializeComponent();
        }

    
        private async void registrateButton_Click(object sender, EventArgs e)
        {
            string nome = nomeTextBox.Text;
            string cognome = cognomeTextBox.Text;
            string citta = cittaTextBot.Text;
            string indirizzo = indirizzoTextBox.Text;
            string email = emailTextBox.Text;          
            string telefono = telefonoTextBox.Text;           
            string pass = passwTextBox.Text;
            string confpass = confpswTextBox.Text;

            Richieste registrationPost = new Richieste();

            // controlli formattazione email e psw
            Regex emailCorretta = new Regex(@"^[\w!#$%&'*+\-/=?\^_`{|}~]+(\.[\w!#$%&'*+\-/=?\^_`{|}~]+)*" + "@"
                + @"((([\-\w]+\.)+[a-zA-Z]{2,4})|(([0-9]{1,3}\.){3}[0-9]{1,3}))$");
            Match controlloEmail = emailCorretta.Match(email);
            Regex pswCorretta = new Regex("^(?!.* )(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[.#?!@$%^&*-]).{8,15}$");
            Match controlloPassword = pswCorretta.Match(pass);
            

            // controllo 1: campi vuoti
            if (nome == String.Empty || cognome == String.Empty || citta == String.Empty || 
                indirizzo == String.Empty || email == String.Empty || telefonoTextBox.Text == String.Empty 
                || pass == String.Empty)
            {
                MessageBox.Show("Attenzione: uno o più campi vuoti", "Controlla i campi", MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                return;
            }
            // controllo 2: password e conferma password
            else if (pass != confpass)
            {
                MessageBox.Show("La password non coincide con la conferma", "Attenzione", MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
                return;
            }
            // controllo 3: formattazione password corretta
            else if (controlloPassword.Success == false)
            {
                MessageBox.Show("La password deve essere da 8 a 15 caratteri e comprendere almeno 1 cifra," +
                    "1 lettera minuscola, 1 maiuscola, 1 carattere speciale e nessuno spazio vuoto",
                    "Errore password", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            // controllo 4: formattazione email corretta
            else if (controlloEmail.Success == false)
            {
                MessageBox.Show("L'email non è valida, controlla la formattazione", "Errore e-mail",
                    MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                return;
            }
            // controllo 5: n. telefono
            else if (telefonoTextBox.Text.All(char.IsDigit) == false || telefonoTextBox.Text.Length != 10)
            {
                MessageBox.Show("Inserisci un numero di telefono valido (+39 va omesso)", "n. cellulare non valido",
                    MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                return;
            }
            
            

            try
            {

                var datiUtente = new Dictionary<string, string>
                {
                    {"nome", nome },
                    {"cognome", cognome },
                    {"citta", citta },
                    {"indirizzo", indirizzo },
                    {"email", email },
                    {"telefono", telefono },
                    {"password", pass }
                };
                var datiDaInviare = new FormUrlEncodedContent(datiUtente);
                var result= await registrationPost.HttpPostAsync("http://localhost:8000/register", datiDaInviare);
               
                // controllo utente esistente
                if (result.Equals("Email esistente") == true)
                {
                    MessageBox.Show("ATTENZIONE: utente già esistente. L'email inserita appartiene" +
                        "a un account già registrato", "Account già esistente", MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
                else if(result.Equals("Errore generico") == true)
                {
                    MessageBox.Show("Non è stato possibile creare il tuo account", "Errore",
                        MessageBoxButtons.OK, MessageBoxIcon.Stop);
                }
                else
                {
                    MessageBox.Show("Il tuo account è stato creato correttamente!", "Success", MessageBoxButtons.OK,
                        MessageBoxIcon.Information);
                    new FormLogin().Show();
                    this.Hide();
                 //   Credenziali c = new Credenziali(email, telefono, pass);
                 //   Utente u = new Utente(nome, cognome, citta, indirizzo, c);
                    
                }
            }
            catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
               
            }
        }

        private void mostrapswCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            if (mostrapswCheckBox.Checked == true)
            {
                passwTextBox.PasswordChar = '\0';
                confpswTextBox.PasswordChar = '\0';
            }
            else
            {
                passwTextBox.PasswordChar = '•';
                confpswTextBox.PasswordChar = '•';
            }
        }

        private void backButton_Click(object sender, EventArgs e)
        {
            new FormLogin().Show();
            this.Hide();
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
