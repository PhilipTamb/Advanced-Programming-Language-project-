namespace ClientUtenteCS.Forms
{
    partial class FormSelezionaProfessionista
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.listViewProfessionisti = new System.Windows.Forms.ListView();
            this.colonnaNome = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaCognome = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaProfessione = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaRecensione = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaCitta = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaId = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.SuspendLayout();
            // 
            // listViewProfessionisti
            // 
            this.listViewProfessionisti.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colonnaNome,
            this.colonnaCognome,
            this.colonnaProfessione,
            this.colonnaRecensione,
            this.colonnaCitta,
            this.colonnaId});
            this.listViewProfessionisti.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.listViewProfessionisti.FullRowSelect = true;
            this.listViewProfessionisti.HideSelection = false;
            this.listViewProfessionisti.Location = new System.Drawing.Point(37, 52);
            this.listViewProfessionisti.Name = "listViewProfessionisti";
            this.listViewProfessionisti.Size = new System.Drawing.Size(600, 389);
            this.listViewProfessionisti.TabIndex = 1;
            this.listViewProfessionisti.UseCompatibleStateImageBehavior = false;
            this.listViewProfessionisti.View = System.Windows.Forms.View.Details;
            this.listViewProfessionisti.MouseClick += new System.Windows.Forms.MouseEventHandler(this.listViewProfessionisti_MouseClick);
            // 
            // colonnaNome
            // 
            this.colonnaNome.Text = "Nome";
            this.colonnaNome.Width = 100;
            // 
            // colonnaCognome
            // 
            this.colonnaCognome.Text = "Cognome";
            this.colonnaCognome.Width = 125;
            // 
            // colonnaProfessione
            // 
            this.colonnaProfessione.Text = "Professione";
            this.colonnaProfessione.Width = 150;
            // 
            // colonnaRecensione
            // 
            this.colonnaRecensione.Text = "Recensione";
            this.colonnaRecensione.Width = 75;
            // 
            // colonnaCitta
            // 
            this.colonnaCitta.Text = "Città";
            this.colonnaCitta.Width = 125;
            // 
            // colonnaId
            // 
            this.colonnaId.Text = "None";
            this.colonnaId.Width = 0;
            // 
            // FormSelezionaProfessionista
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(668, 492);
            this.Controls.Add(this.listViewProfessionisti);
            this.Name = "FormSelezionaProfessionista";
            this.Text = "FormSelezionaProfessionista";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView listViewProfessionisti;
        private System.Windows.Forms.ColumnHeader colonnaNome;
        private System.Windows.Forms.ColumnHeader colonnaCognome;
        private System.Windows.Forms.ColumnHeader colonnaProfessione;
        private System.Windows.Forms.ColumnHeader colonnaRecensione;
        private System.Windows.Forms.ColumnHeader colonnaCitta;
        private System.Windows.Forms.ColumnHeader colonnaId;
    }
}