namespace ClientUtenteCS.Forms
{
    partial class FormRecensione
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
            this.comboBox = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.textBoxIdicket = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.comboBoxValutazione = new System.Windows.Forms.ComboBox();
            this.buttonVote = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // comboBox
            // 
            this.comboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBox.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.comboBox.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.comboBox.FormattingEnabled = true;
            this.comboBox.Location = new System.Drawing.Point(38, 95);
            this.comboBox.Name = "comboBox";
            this.comboBox.Size = new System.Drawing.Size(484, 28);
            this.comboBox.TabIndex = 0;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label2.Location = new System.Drawing.Point(34, 44);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(289, 20);
            this.label2.TabIndex = 4;
            this.label2.Text = "Seleziona il professionista da recensire";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label1.Location = new System.Drawing.Point(34, 172);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(586, 20);
            this.label1.TabIndex = 5;
            this.label1.Text = "Inserisci il numero del ticket di cui vuoi valutare le prestazioni del profession" +
    "ista";
            // 
            // textBoxIdicket
            // 
            this.textBoxIdicket.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.textBoxIdicket.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.textBoxIdicket.Font = new System.Drawing.Font("Microsoft YaHei", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBoxIdicket.Location = new System.Drawing.Point(38, 211);
            this.textBoxIdicket.Name = "textBoxIdicket";
            this.textBoxIdicket.Size = new System.Drawing.Size(73, 25);
            this.textBoxIdicket.TabIndex = 9;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label3.Location = new System.Drawing.Point(34, 290);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(128, 20);
            this.label3.TabIndex = 10;
            this.label3.Text = "Seleziona il voto";
            // 
            // comboBoxValutazione
            // 
            this.comboBoxValutazione.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxValutazione.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.comboBoxValutazione.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBoxValutazione.FormattingEnabled = true;
            this.comboBoxValutazione.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5"});
            this.comboBoxValutazione.Location = new System.Drawing.Point(211, 286);
            this.comboBoxValutazione.Name = "comboBoxValutazione";
            this.comboBoxValutazione.Size = new System.Drawing.Size(76, 24);
            this.comboBoxValutazione.TabIndex = 11;
            // 
            // buttonVote
            // 
            this.buttonVote.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonVote.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonVote.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.buttonVote.Location = new System.Drawing.Point(266, 414);
            this.buttonVote.Name = "buttonVote";
            this.buttonVote.Size = new System.Drawing.Size(107, 32);
            this.buttonVote.TabIndex = 15;
            this.buttonVote.Text = "Vota";
            this.buttonVote.UseVisualStyleBackColor = true;
            this.buttonVote.Click += new System.EventHandler(this.buttonVote_Click);
            // 
            // FormRecensione
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(668, 492);
            this.Controls.Add(this.buttonVote);
            this.Controls.Add(this.comboBoxValutazione);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.textBoxIdicket);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.comboBox);
            this.Name = "FormRecensione";
            this.Text = "FormRecensione";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox comboBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBoxIdicket;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox comboBoxValutazione;
        private System.Windows.Forms.Button buttonVote;
    }
}