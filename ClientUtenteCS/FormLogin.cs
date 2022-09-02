using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Diagnostics;
using System.Net.Http;

namespace ClientUtenteCS
{
    public partial class FormLogin : Form
    {

        public static string emailUtente;
        public FormLogin()
        {
            InitializeComponent();
        }

        private async void loginButton_Click(object sender, EventArgs e)
        {
            Richieste loginPost = new Richieste();

            string email = emailTextBox.Text;
            string pass = passwTextBox.Text;

            if (email == String.Empty || pass == String.Empty)
            {
                MessageBox.Show("Attenzione: uno o più campi vuoti", "Controlla i campi", MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
            }

            try
            {
                var datiUtente = new Dictionary<string, string>
                {
                    {"email", email },
                    {"password", pass }
                };

                var datiDaInviare = new FormUrlEncodedContent(datiUtente);
                var result = await loginPost.HttpPostAsync("http://localhost:8000/login", datiDaInviare);

                if (result.Equals("Credenziali errati"))
                {
                    MessageBox.Show("L'email o la password sono errati. Ricontrolla i dati",
                        "Login error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    
                }
                else if (result.Equals("Errore generico"))
                {
                    MessageBox.Show("Qualcosa è andato storto", "Errore",
                        MessageBoxButtons.OK, MessageBoxIcon.Stop);
                
                }
                else
                {
                    emailUtente = email;
                    new FormHomepage().Show();
                    this.Hide();
                }

            }
            catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void registerLabel_Click(object sender, EventArgs e)
        {
            new RegisterForm().Show();          
            this.Hide();

        }

        private void mostrapswCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            if (mostrapswCheckBox.Checked == true)
            {
                passwTextBox.PasswordChar = '\0';
            }
            else
            {
                passwTextBox.PasswordChar = '•';
            }
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
