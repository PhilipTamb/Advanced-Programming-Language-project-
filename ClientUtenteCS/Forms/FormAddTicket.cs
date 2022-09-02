using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Diagnostics;
using System.Net.Http;

namespace ClientUtenteCS.Forms
{
    public partial class FormAddTicket : Form
    {
        public static bool selectProfessionista = false;
        public FormAddTicket()
        {
            InitializeComponent();
        }

        private async void buttonCreateTicket_Click(object sender, EventArgs e)
        {
            Richieste createTicket = new Richieste();
            
            string titolo = textTitoloTicket.Text;
            string categoria = comboBoxCategoriaTicket.Text;
            string descrizione = textBoxDescrTicket.Text;
            string userEmail = FormLogin.emailUtente;

            if (titolo == String.Empty || categoria == String.Empty || descrizione == String.Empty) {
                MessageBox.Show("Attenzione: uno o più campi vuoti", "Controlla i campi", MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                return;
            }

            try
            {
                var datiTicket = new Dictionary<string, string>
                {
                    {"titolo", titolo },
                    {"categoria", categoria },
                    {"descrizione", descrizione },
                    {"email", userEmail}
                };

                var datiDaInviare = new FormUrlEncodedContent(datiTicket);
                var result = await createTicket.HttpPostAsync("http://localhost:8000/newticket", datiDaInviare);

                if (result.Equals("Utente non trovato") || result.Equals("Errore generico"))
                {
                    MessageBox.Show("Qualcosa è andato storto", "Errore",
                       MessageBoxButtons.OK, MessageBoxIcon.Stop);
                   
                }
                else
                {
                    MessageBox.Show("Il ticket è stato creato correttamente, si prega adesso di selezionare" +
                        " un professionista", "Ticket OK", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    FormSelezionaProfessionista.passingTicketInformation(categoria);
                    selectProfessionista = true;
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

  
    }
}
