using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Net.Http;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace ClientUtenteCS.Forms
{
    public partial class FormDownloadFattura : Form
    {
        public FormDownloadFattura()
        {
            InitializeComponent();
        }

        private async void buttonDownload_Click(object sender, EventArgs e)
        {
            Richieste scaricaFattura = new Richieste();
            string idTicket = textBoxIdicket.Text;

            if (idTicket == String.Empty)
            {
                MessageBox.Show("Attenzione: uno o più campi vuoti", "Controlla i campi", MessageBoxButtons.OK,
                   MessageBoxIcon.Warning);
                return;
            }

            try
            {
                var datiUtente = new Dictionary<string, string>
                {
                    {"id_utente", FormLogin.idUtente},
                    {"id_ticket", idTicket}
                };
               
                var datiDaInviare = new FormUrlEncodedContent(datiUtente);
                var result = await scaricaFattura.HttpPostAsync("http://localhost:8000/downloadfattura", datiDaInviare);

                if (result.Equals("Errore generico"))
                {
                    MessageBox.Show("Qualcosa è andato storto", "Errore",
                       MessageBoxButtons.OK, MessageBoxIcon.Stop);
                }
                else if (result.Equals("Non disponibile") || string.IsNullOrEmpty(result)) 
                {
                    MessageBox.Show("Il ticket inserito non ha ancora la fattura pronta oppure il numero è" +
                        " errato. Controlla lo stato del ticket e il suo numero di riferimento e riprova",
                        "Error: fattura not found", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    downloadFattura(result, idTicket);
                }


            } catch (Exception exc)
            {
                Debug.WriteLine(exc);
                MessageBox.Show("Non è possibile contattare il server in questo momento. Riprova più tardi.",
                    "Server error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }


        private void downloadFattura(string linkFattura, string id_ticket)
        {
            string pathSave;
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
            {
                pathSave = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
            }
            else
            {
                // di default l'applicazione salva le fatture nel desktop
                pathSave = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            }

            using (WebClient wc = new WebClient())
            {
                wc.DownloadProgressChanged += wc_DownloadProgressChanged;
                wc.DownloadFileAsync(
                    // Param1 = Link of file
                    // http://localhost/img/module_table_top.png
                    new System.Uri(linkFattura),
                    // Param2 = Path to save
                    pathSave + "/fattura" + id_ticket + ".pdf"
                );
            }
            MessageBox.Show("Download completato!", "OK", MessageBoxButtons.OK, MessageBoxIcon.Information);

        }
        private void wc_DownloadProgressChanged(object sender, DownloadProgressChangedEventArgs e)
        {
            progressBar.Value = e.ProgressPercentage;
        }
    }
}
