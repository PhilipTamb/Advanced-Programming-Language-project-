using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Windows.Forms;

namespace ClientUtenteCS.Forms
{
    public partial class FormViewPreventivi : Form
    {
        public static bool preventivoInfo = false;
        public static string idPreventivo;
        public FormViewPreventivi()
        {
            InitializeComponent();
            loadPreventivi();
        }



        private void listViewPreventivi_MouseClick(object sender, MouseEventArgs e)
        {
            for (int i = 0; i < listViewPreventivi.Items.Count; i++)
            {
                idPreventivo = listViewPreventivi.SelectedItems[0].SubItems[4].Text;
                var rectangle = listViewPreventivi.GetItemRect(i);
                if (rectangle.Contains(e.Location))
                {
                    preventivoInfo = true;
                    this.Hide();

                }
            }
        }

        private async void loadPreventivi()
        {
            Richieste getPreventivi = new Richieste();

            try
            {
                var mail = new Dictionary<string, string>
                {
                    {"email", FormLogin.emailUtente}
                };
                var datiDaInviare = new FormUrlEncodedContent(mail);
                var result = await getPreventivi.HttpPostAsync("http://localhost:8000/getpreventivi", datiDaInviare);
                List<Preventivo> arrayPreventivi = JsonConvert.DeserializeObject<List<Preventivo>>(result);

                if (arrayPreventivi != null)
                {
                    foreach (var item in arrayPreventivi)
                    {
                        listViewPreventivi.Items.Add(new ListViewItem(new String[] { item.IdTicket.ToString(), item.Costo.ToString(), item.DataOra, item.Descrizione, item.Id.ToString() }));
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
