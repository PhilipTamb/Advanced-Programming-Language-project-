namespace ClientUtenteCS.Forms
{
    partial class FormViewTickets
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
            this.listViewTickets = new System.Windows.Forms.ListView();
            this.colonnaNumTicket = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaTitolo = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaCategoria = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colonnaStato = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.SuspendLayout();
            // 
            // listViewTickets
            // 
            this.listViewTickets.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colonnaNumTicket,
            this.colonnaTitolo,
            this.colonnaCategoria,
            this.colonnaStato});
            this.listViewTickets.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.listViewTickets.FullRowSelect = true;
            this.listViewTickets.HideSelection = false;
            this.listViewTickets.Location = new System.Drawing.Point(33, 60);
            this.listViewTickets.Name = "listViewTickets";
            this.listViewTickets.Size = new System.Drawing.Size(595, 389);
            this.listViewTickets.TabIndex = 0;
            this.listViewTickets.UseCompatibleStateImageBehavior = false;
            this.listViewTickets.View = System.Windows.Forms.View.Details;
            // 
            // colonnaNumTicket
            // 
            this.colonnaNumTicket.Text = "Numero";
            this.colonnaNumTicket.Width = 100;
            // 
            // colonnaTitolo
            // 
            this.colonnaTitolo.Text = "Titolo";
            this.colonnaTitolo.Width = 250;
            // 
            // colonnaCategoria
            // 
            this.colonnaCategoria.Text = "Categoria";
            this.colonnaCategoria.Width = 160;
            // 
            // colonnaStato
            // 
            this.colonnaStato.Text = "Stato";
            this.colonnaStato.Width = 150;
            // 
            // FormViewTickets
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(668, 492);
            this.Controls.Add(this.listViewTickets);
            this.Name = "FormViewTickets";
            this.Text = "FormViewTickets";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView listViewTickets;
        private System.Windows.Forms.ColumnHeader colonnaNumTicket;
        private System.Windows.Forms.ColumnHeader colonnaTitolo;
        private System.Windows.Forms.ColumnHeader colonnaCategoria;
        private System.Windows.Forms.ColumnHeader colonnaStato;
    }
}