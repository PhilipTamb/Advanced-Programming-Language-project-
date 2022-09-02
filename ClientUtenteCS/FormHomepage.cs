using System;
using System.Collections.Generic;
using System.Drawing;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;
using System.Diagnostics;

namespace ClientUtenteCS
{
    public partial class FormHomepage : Form
    {

        // campi
        private Button bottoneCorrente;
        private Random random;
        private int indiceTemp;
        private Form formAttivo;
        private string nomeUtente;
        private bool addTicketBool;
        private bool viewPreventiviBool;

        //costruttori
        public FormHomepage()
        {
            InitializeComponent();
            random = new Random();
            buttonBackHome.Visible = false;
            this.Text = String.Empty;
            this.ControlBox = false;
            getNomeUtente();
            
        }

        // metodi
        private Color SelezionaTemaColore()
        {
            ColoreTema tema = new ColoreTema();
            int indice = random.Next(tema.ListaColori.Count);
            // per randomizzare il tema del colore della finestra form
            while (indiceTemp == indice)
            {
               indice=  random.Next(tema.ListaColori.Count);
            }
            indiceTemp = indice;
            string colore = tema.ListaColori[indice];
            return ColorTranslator.FromHtml(colore);
        }

        // cambiamenti del colore e del font dei bottoni al click
        private void bottoneAttivo(object bottone)
        {
            if (bottone != null)
            {
                if (bottoneCorrente != (Button)bottone)
                {
                    bottoneDisattivo();
                    Color colore = SelezionaTemaColore();
                    bottoneCorrente = (Button)bottone;
                    bottoneCorrente.BackColor = colore;
                    bottoneCorrente.ForeColor = Color.White;
                    bottoneCorrente.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.00F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
                    panelTitle.BackColor = colore;
                    buttonBackHome.Visible = true;
                }
            }
        }

        private void bottoneDisattivo ()
        {
            foreach (Control bottoni in panelMenu.Controls)
            {
                if (bottoni.GetType() == typeof(Button))
                {
                    bottoni.BackColor = Color.FromArgb(178, 34, 34);
                    bottoni.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
                }
            }
        }

        // metodo per aprire altri form all'interno del pannello dove si cliccano le varie voci del menu
        private void OpenForms(Form formFiglio, object bottone)
        {
            if (formAttivo != null)
            {
                formAttivo.Close();
            }
            bottoneAttivo(bottone);
            formAttivo = formFiglio;
            formFiglio.TopLevel = false;
            formFiglio.FormBorderStyle= FormBorderStyle.None;
            formFiglio.Dock= DockStyle.Fill;
            this.panelSottostante.Controls.Add(formFiglio);
            this.panelSottostante.Tag = formFiglio;
            formFiglio.BringToFront();
            formFiglio.Show();
         //   labelTitle.Text = formFiglio.Text;

        }


        private async void buttonAddTicket_Click(object sender, EventArgs e)
        {
            addTicketBool = true;
            viewPreventiviBool = false;
            labelTitle.Text = "CREAZIONE TICKET";
            OpenForms(new Forms.FormAddTicket(), sender);
            while (true)
            {
                await Task.Delay(1000);
                

                if (Forms.FormAddTicket.selectProfessionista == true)
                {
                    labelTitle.Text = "SELEZIONA PROFESSIONISTA";
                    OpenForms(new Forms.FormSelezionaProfessionista(), sender);
                    break;
                }
                else if (addTicketBool == false)
                {
                    // per evitare che il loop non si chiuda qualora l'utente passi in altre funzioni senza
                    // creare il ticket e selezionare il professionista
                    break;
                }
            }
    
           
        }

        private void buttonViewTicket_Click(object sender, EventArgs e)
        {
            if (Forms.FormAddTicket.selectProfessionista == false)
            {
                addTicketBool = false;
                viewPreventiviBool = false;
                OpenForms(new Forms.FormViewTickets(), sender);
                labelTitle.Text = "I TUOI TICKET";
            }
            else
            {
                MessageBox.Show("Per poter proseguire è necessario selezionare un professionista" +
                    " per il ticket appena creato", "Attenzione!", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private async void buttonPreventivi_Click(object sender, EventArgs e)
        {
            if (Forms.FormAddTicket.selectProfessionista == false)
            {
                addTicketBool = false;
                viewPreventiviBool = true;
                OpenForms(new Forms.FormViewPreventivi(), sender);
                labelTitle.Text = "I TUOI PREVENTIVI";

                while (true)
                {
                    await Task.Delay(1000);

                    if (Forms.FormViewPreventivi.preventivoInfo == true)
                    {
                        labelTitle.Text = "DETTAGLI DEL PREVENTIVO";
                        OpenForms(new Forms.FormInfoPreventivo(), sender);
                        break;
                    }
                    else if (viewPreventiviBool == false)
                    {
                        break;
                    }
                }
            }
            else
            {
                MessageBox.Show("Per poter proseguire è necessario selezionare un professionista" +
                    " per il ticket appena creato", "Attenzione!", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void buttonFatture_Click(object sender, EventArgs e)
        {
            if (Forms.FormAddTicket.selectProfessionista == false)
            {
                addTicketBool = false;
                viewPreventiviBool = false;
                labelTitle.Text = "LE TUE FATTURE";
                OpenForms(new Forms.FormDownloadFattura(), sender);
            }
            else
            {
                MessageBox.Show("Per poter proseguire è necessario selezionare un professionista" +
                    " per il ticket appena creato", "Attenzione!", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void buttonReview_Click(object sender, EventArgs e)
        {
            if (Forms.FormAddTicket.selectProfessionista == false)
            {
                addTicketBool = false;
                viewPreventiviBool = false;
                labelTitle.Text = "LE TUE OPINIONI";
                OpenForms(new Forms.FormRecensione(), sender);
            }
            else
            {
                MessageBox.Show("Per poter proseguire è necessario selezionare un professionista" +
                    " per il ticket appena creato", "Attenzione!", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void buttonBackHome_Click(object sender, EventArgs e)
        {
            if (Forms.FormAddTicket.selectProfessionista == false)
            {
                addTicketBool = false;
                viewPreventiviBool = false;
                if (formAttivo != null)
                {
                    formAttivo.Close();
                }
                Reset();
            }
            else
            {
                MessageBox.Show("Per poter proseguire è necessario selezionare un professionista" +
                    " per il ticket appena creato", "Attenzione!", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
        // ritorno all'homepage
        private void Reset()
        {
            bottoneDisattivo();
            labelTitle.Text = "Benvenuto, " + nomeUtente;
            panelTitle.BackColor = Color.FromArgb(128, 0, 0);
            bottoneCorrente = null;
            buttonBackHome.Visible = false;
        }

        private async void getNomeUtente()
        {
            Richieste getNome = new Richieste();

            try
            {
                var mail = new Dictionary<string, string>
                {
                    {"email", FormLogin.emailUtente}
                };
                var datiDaInviare = new FormUrlEncodedContent(mail);
                var result = await getNome.HttpPostAsync("http://localhost:8000/getnome", datiDaInviare);

                if (result.Equals("Errore generico"))
                {
                    MessageBox.Show("Qualcosa è andato storto, per favore riavvia l'applicazione", "Utente" +
                        " non riconosciuto", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    nomeUtente = result;
                }
                labelTitle.Text = "Benvenuto, " + nomeUtente;
            }
             catch (Exception exc)
            {
                Debug.WriteLine(exc);
            }
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
