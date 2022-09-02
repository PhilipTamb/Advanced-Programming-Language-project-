using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Windows.Forms;
using Newtonsoft.Json;

namespace ClientUtenteCS.Forms
{
    public partial class FormSelezionaProfessionista : Form
    {
        private static String category;

        public FormSelezionaProfessionista()
        {
            InitializeComponent();
            loadProfessionisti();
        }
        public static void passingTicketInformation(String categoria)
        {
            category = categoria;
        }

        private async void listViewProfessionisti_MouseClick(object sender, MouseEventArgs e)
        {
            // PRENDERE L'ID DEL PROFESSIONISTA DEL TICKET SCELTO

            for (int i = 0; i < listViewProfessionisti.Items.Count; i++)
            {
                Richieste selectProfessionista = new Richieste();
                string userEmail = FormLogin.emailUtente;
                string idProfessionista = listViewProfessionisti.SelectedItems[0].SubItems[5].Text;
                var rectangle = listViewProfessionisti.GetItemRect(i);
                if (rectangle.Contains(e.Location))
                {
                    DialogResult diagRes= MessageBox.Show("Vuoi scegliere questo specialista per il tuo ticket?", "Selezione",
                        MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                    if (diagRes == DialogResult.Yes)
                    {
                        try
                        {
                            var datiConfermaProfessionista = new Dictionary<string, string>
                            {
                                {"email", userEmail },
                                {"idProfessionista", idProfessionista }
                            };

                            var datiDaInviare = new FormUrlEncodedContent(datiConfermaProfessionista);
                            var result = await selectProfessionista.HttpPostAsync("http://localhost:8000/selectprofessionista", datiDaInviare);
                            
                            if (result.Equals("Errore generico"))
                            {
                                MessageBox.Show("Qualcosa è andato storto", "Errore", MessageBoxButtons.OK, MessageBoxIcon.Stop);
                            }
                            else
                            {
                                MessageBox.Show("Il professionista è stato contattato. Se accetta, riceverai un suo preventivo nell'apposita sezione." +
                                    " Controlla periodicamente I TUOI PREVENTIVI", "Ticket completo", MessageBoxButtons.OK,
                                    MessageBoxIcon.Information);
                                FormAddTicket.selectProfessionista = false;
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
                    return;
                }
            }
        }

        private async void loadProfessionisti()
        {
            Richieste getProfessionisti = new Richieste();

            try
            {
                var categ = new Dictionary<string, string>
                {
                    {"categoria", category }
                };

                var datiDaInviare = new FormUrlEncodedContent(categ);
                var result = await getProfessionisti.HttpPostAsync("http://localhost:8000/getprofessionisti", datiDaInviare);

                List<Professionista> arrayProfessionisti = JsonConvert.DeserializeObject<List<Professionista>>(result);
                if (arrayProfessionisti == null)
                {
                    MessageBox.Show("Non è disponibile alcun professionista per la categoria da te indicata :(",
                    "Ci dispiace", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                    FormAddTicket.selectProfessionista = false;
                    this.Hide();
                }
                else {               
                    foreach (var item in arrayProfessionisti)
                    {
                        // la colonna 5 nella listview non è visualizzabile, serve solo per prelevare l'id
                        // del professionista cliccato dall'utente
                        if (item.Recensione <= 0)
                        {
                            listViewProfessionisti.Items.Add(new ListViewItem(new String[] { item.Nome, item.Cognome, item.Professione, "N/A", item.Citta, item.Id.ToString() }));
                        }
                        else
                        {
                            listViewProfessionisti.Items.Add(new ListViewItem(new String[] { item.Nome, item.Cognome, item.Professione, item.Recensione.ToString(), item.Citta, item.Id.ToString() }));
                        }
                    }
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
