namespace ClientUtenteCS.Forms
{
    partial class FormAddTicket
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
            this.textTitoloTicket = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.textBoxDescrTicket = new System.Windows.Forms.TextBox();
            this.buttonCreateTicket = new System.Windows.Forms.Button();
            this.comboBoxCategoriaTicket = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textTitoloTicket
            // 
            this.textTitoloTicket.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.textTitoloTicket.Font = new System.Drawing.Font("Microsoft YaHei", 9.75F);
            this.textTitoloTicket.Location = new System.Drawing.Point(123, 30);
            this.textTitoloTicket.Name = "textTitoloTicket";
            this.textTitoloTicket.Size = new System.Drawing.Size(254, 18);
            this.textTitoloTicket.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label1.Location = new System.Drawing.Point(24, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 20);
            this.label1.TabIndex = 2;
            this.label1.Text = "Titolo";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label3.Location = new System.Drawing.Point(24, 264);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(93, 20);
            this.label3.TabIndex = 4;
            this.label3.Text = "Descrizione";
            // 
            // textBoxDescrTicket
            // 
            this.textBoxDescrTicket.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.textBoxDescrTicket.Font = new System.Drawing.Font("Microsoft YaHei", 9.75F);
            this.textBoxDescrTicket.Location = new System.Drawing.Point(123, 148);
            this.textBoxDescrTicket.Multiline = true;
            this.textBoxDescrTicket.Name = "textBoxDescrTicket";
            this.textBoxDescrTicket.Size = new System.Drawing.Size(301, 211);
            this.textBoxDescrTicket.TabIndex = 5;
            // 
            // buttonCreateTicket
            // 
            this.buttonCreateTicket.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonCreateTicket.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonCreateTicket.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.buttonCreateTicket.Location = new System.Drawing.Point(294, 402);
            this.buttonCreateTicket.Name = "buttonCreateTicket";
            this.buttonCreateTicket.Size = new System.Drawing.Size(107, 32);
            this.buttonCreateTicket.TabIndex = 6;
            this.buttonCreateTicket.Text = "Crea";
            this.buttonCreateTicket.UseVisualStyleBackColor = true;
            this.buttonCreateTicket.Click += new System.EventHandler(this.buttonCreateTicket_Click);
            // 
            // comboBoxCategoriaTicket
            // 
            this.comboBoxCategoriaTicket.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxCategoriaTicket.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.comboBoxCategoriaTicket.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBoxCategoriaTicket.FormattingEnabled = true;
            this.comboBoxCategoriaTicket.Items.AddRange(new object[] {
            "Edilizia",
            "Idraulica",
            "Falegnameria",
            "Giardinaggio",
            "Climatizzazione e riscaldamento",
            "Telecomunicazioni",
            "Rete elettrica ed elettrodomestici"});
            this.comboBoxCategoriaTicket.Location = new System.Drawing.Point(123, 89);
            this.comboBoxCategoriaTicket.Name = "comboBoxCategoriaTicket";
            this.comboBoxCategoriaTicket.Size = new System.Drawing.Size(199, 24);
            this.comboBoxCategoriaTicket.TabIndex = 7;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label2.Location = new System.Drawing.Point(24, 89);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(80, 20);
            this.label2.TabIndex = 8;
            this.label2.Text = "Categoria";
            // 
            // FormAddTicket
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(668, 492);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.comboBoxCategoriaTicket);
            this.Controls.Add(this.buttonCreateTicket);
            this.Controls.Add(this.textBoxDescrTicket);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textTitoloTicket);
            this.Name = "FormAddTicket";
            this.Text = "FormSecondari";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textTitoloTicket;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBoxDescrTicket;
        private System.Windows.Forms.Button buttonCreateTicket;
        private System.Windows.Forms.ComboBox comboBoxCategoriaTicket;
        private System.Windows.Forms.Label label2;
    }
}