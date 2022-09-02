namespace ClientUtenteCS.Forms
{
    partial class FormViewPreventivi
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
            this.listViewPreventivi = new System.Windows.Forms.ListView();
            this.colonnaIdTicket = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaCosto = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaDataOra = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaDescrizione = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaIdPreventivo = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.SuspendLayout();
            // 
            // listViewPreventivi
            // 
            this.listViewPreventivi.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colonnaIdTicket,
            this.colonnaCosto,
            this.colonnaDataOra,
            this.colonnaDescrizione,
            this.colonnaIdPreventivo});
            this.listViewPreventivi.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.listViewPreventivi.FullRowSelect = true;
            this.listViewPreventivi.HideSelection = false;
            this.listViewPreventivi.Location = new System.Drawing.Point(37, 44);
            this.listViewPreventivi.Name = "listViewPreventivi";
            this.listViewPreventivi.Size = new System.Drawing.Size(595, 389);
            this.listViewPreventivi.TabIndex = 0;
            this.listViewPreventivi.UseCompatibleStateImageBehavior = false;
            this.listViewPreventivi.View = System.Windows.Forms.View.Details;
            this.listViewPreventivi.MouseClick += new System.Windows.Forms.MouseEventHandler(this.listViewPreventivi_MouseClick);
            // 
            // colonnaIdTicket
            // 
            this.colonnaIdTicket.Text = "Ticket di riferimento";
            this.colonnaIdTicket.Width = 168;
            // 
            // colonnaCosto
            // 
            this.colonnaCosto.Text = "Costo";
            this.colonnaCosto.Width = 81;
            // 
            // colonnaDataOra
            // 
            this.colonnaDataOra.Text = "Data & ora";
            this.colonnaDataOra.Width = 142;
            // 
            // colonnaDescrizione
            // 
            this.colonnaDescrizione.Text = "Descrizione";
            this.colonnaDescrizione.Width = 183;
            // 
            // colonnaIdPreventivo
            // 
            this.colonnaIdPreventivo.Text = "IdPreventivo";
            this.colonnaIdPreventivo.Width = 0;
            // 
            // FormViewPreventivi
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(668, 492);
            this.Controls.Add(this.listViewPreventivi);
            this.Name = "FormViewPreventivi";
            this.Text = "FormViewPreventivi";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView listViewPreventivi;
        private System.Windows.Forms.ColumnHeader colonnaIdTicket;
        private System.Windows.Forms.ColumnHeader colonnaCosto;
        private System.Windows.Forms.ColumnHeader colonnaDataOra;
        private System.Windows.Forms.ColumnHeader colonnaDescrizione;
        private System.Windows.Forms.ColumnHeader colonnaIdPreventivo;
    }
}