using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Windows.Forms;

namespace ClientUtenteCS.Forms
{
    public partial class FormInfoPreventivo : Form
    {
        public FormInfoPreventivo()
        {
            InitializeComponent();
            loadInfoPreventivo();
        }


        private async void buttonAccetta_click(object sender, EventArgs e)
        {
            Richieste accettaPreventivo = new Richieste();

            try
            {
                var id = new Dictionary<string, string>
                {
                    {"id", FormViewPreventivi.idPreventivo }
                };
                var datiDaInviare = new FormUrlEncodedContent(id);
                var result = await accettaPreventivo.HttpPostAsync("http://localhost:8000/acceptpreventivo", datiDaInviare);

                if (result.Equals("Preventivo accettato"))
                {
                    MessageBox.Show("Preventivo accettato: il ticket sarà concluso non appena il lavoratore," +
                        "ultimato il lavoro, invierà la fattura che potrai consultare nella sezione apposita. Puoi" +
                        " anche lasciare una recensione a lavoro terminato", "Ticket in corso",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                    this.Hide();
                }
                else
                {
                    MessageBox.Show("Qualcosa è andato storto", "Errore",
                        MessageBoxButtons.OK, MessageBoxIcon.Stop);
                }
            } catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private async void buttonRifiuta_click(object sender, EventArgs e)
        {
            Richieste rifiutaPreventivo = new Richieste();

            try
            {
                var id = new Dictionary<string, string>
                {
                    {"id", FormViewPreventivi.idPreventivo }
                };
                var datiDaInviare = new FormUrlEncodedContent(id);
                var result = await rifiutaPreventivo.HttpPostAsync("http://localhost:8000/denypreventivo", datiDaInviare);

                if (result.Equals("Preventivo rifiutato"))
                {
                    MessageBox.Show("Preventivo rifiutato: se il tuo problema non è stato ancora" +
                        " risolto, puoi creare un altro ticket selezionando un altro professionista." +
                        " Se il preventivo non era soddisfacente ricordati questa volta di inserire" +
                        " nella descrizione del ticket informazioni aggiuntive utili (limiti di orario," +
                        " limiti di prezzo, tempestività della risoluzione del problema...)", "Ticket rifiutato",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                    this.Hide();
                }
                else
                {
                    MessageBox.Show("Qualcosa è andato storto", "Errore",
                        MessageBoxButtons.OK, MessageBoxIcon.Stop);
                }
            }
            catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }


        private async void loadInfoPreventivo()
        {
            Richieste getInfoPreventivo = new Richieste();

            try
            {
                var id = new Dictionary<string, string>
                {
                    {"id", FormViewPreventivi.idPreventivo }
                };
                var datiDaInviare = new FormUrlEncodedContent(id);
                var result = await getInfoPreventivo.HttpPostAsync("http://localhost:8000/getinfopreventivo", datiDaInviare);
                Preventivo infoPreventivo= JsonConvert.DeserializeObject<Preventivo>(result);

                textBoxIdPreventivo.AppendText("" + infoPreventivo.Id);
                textBoxIdTicket.AppendText("" + infoPreventivo.IdTicket);
                textBoxDescrizione.AppendText(infoPreventivo.Descrizione);
                textBoxCosto.AppendText("" + infoPreventivo.Costo);
                textBoxMaterialiRicambi.AppendText(infoPreventivo.MaterialiRicambi);
                textBoxDataOra.AppendText(infoPreventivo.DataOra);

                FormViewPreventivi.preventivoInfo = false;

            } catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

      
    }
}
