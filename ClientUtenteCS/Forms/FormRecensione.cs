using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Windows.Forms;

namespace ClientUtenteCS.Forms
{
    public partial class FormRecensione : Form
    {
        public FormRecensione()
        {
            InitializeComponent();
            loadProfessionistiDaRecensire();
        }


        private async void loadProfessionistiDaRecensire()
        {
            Richieste getProfessionistiDaRecensire = new Richieste();

            try
            {
                var userId = new Dictionary<string, string>
                {
                    {"id_utente", FormLogin.idUtente }
                };


                var datiDaInviare = new FormUrlEncodedContent(userId);
                var result = await getProfessionistiDaRecensire.HttpPostAsync("http://localhost:8000/getprofessionistidavotare", datiDaInviare);

                List<Professionista> arrayProfessionisti = JsonConvert.DeserializeObject<List<Professionista>>(result);
                Dictionary<int, string> myDictionary = new Dictionary<int, string>();

                if (arrayProfessionisti != null)
                {
                    foreach (var item in arrayProfessionisti)
                    {
                        if (item.Recensione <= 0)
                        {
                            myDictionary.Add(item.Id, item.Nome + " " + item.Cognome + " " + item.Citta
                            + " media recensioni= N/A");
                        }
                        else
                        {
                            myDictionary.Add(item.Id, item.Nome + " " + item.Cognome + " " + item.Citta
                                + " media recensioni= " + item.Recensione);
                        }
                      
                        
                    }
                    comboBox.DataSource = myDictionary.ToArray();
                    comboBox.DisplayMember = "Value";
                    comboBox.ValueMember = "Key";
                } else
                {
                    MessageBox.Show("Nessuna recensione da aggiungere", "!", MessageBoxButtons.OK,
                   MessageBoxIcon.Warning);
                    this.Hide();
                }

            } catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private async void buttonVote_Click(object sender, EventArgs e)
        {
  
            Richieste votaProfessionista = new Richieste();
            string idProfessionista = comboBox.SelectedValue.ToString(); 
            string idTicket = textBoxIdicket.Text;
            string voto = comboBoxValutazione.Text;

            if (idProfessionista == String.Empty || idTicket == String.Empty || voto == String.Empty)
            {
                MessageBox.Show("Attenzione: uno o più campi vuoti", "Controlla i campi", MessageBoxButtons.OK,
                   MessageBoxIcon.Warning);
                return;
            }

            try
            {
                var datiValutazione = new Dictionary<string, string>
                {
                    {"id_utente", FormLogin.idUtente },
                    {"id_ticket", idTicket },
                    {"voto", voto },
                    {"id_professionista", idProfessionista }
                };

                var datiDaInviare = new FormUrlEncodedContent(datiValutazione);
                var result = await votaProfessionista.HttpPostAsync("http://localhost:8000/voteprofessionista", datiDaInviare);

                if (result.Equals("Errore generico"))
                {
                    MessageBox.Show("Qualcosa è andato storto", "Errore",
                      MessageBoxButtons.OK, MessageBoxIcon.Stop);
                } else if (result.Equals("Check fallito"))
                {
                    MessageBox.Show("Il ticket inserito non è stato svolto dal professionista da te indicato" +
                        ", oppure il numero è errato. Controlla il numero del ticket nella sezione apposita e riprova",
                       "Error: wrong ticket or professionist", MessageBoxButtons.OK, MessageBoxIcon.Error);
                } else
                {
                    MessageBox.Show("Il tuo voto è stato aggiunto correttamente!", "Review completed", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    this.Hide();
                }

            } catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }

        }
    }
}
