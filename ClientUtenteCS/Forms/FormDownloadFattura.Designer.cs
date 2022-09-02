namespace ClientUtenteCS.Forms
{
    partial class FormDownloadFattura
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
            this.label2 = new System.Windows.Forms.Label();
            this.textBoxIdicket = new System.Windows.Forms.TextBox();
            this.buttonDownload = new System.Windows.Forms.Button();
            this.progressBar = new System.Windows.Forms.ProgressBar();
            this.SuspendLayout();
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.label2.Location = new System.Drawing.Point(12, 134);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(426, 20);
            this.label2.TabIndex = 3;
            this.label2.Text = "Inserisci il numero del ticket di cui vuoi scaricare la fattura";
            // 
            // textBoxIdicket
            // 
            this.textBoxIdicket.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.textBoxIdicket.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.textBoxIdicket.Font = new System.Drawing.Font("Microsoft YaHei", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBoxIdicket.Location = new System.Drawing.Point(466, 133);
            this.textBoxIdicket.Name = "textBoxIdicket";
            this.textBoxIdicket.Size = new System.Drawing.Size(73, 25);
            this.textBoxIdicket.TabIndex = 8;
            // 
            // buttonDownload
            // 
            this.buttonDownload.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonDownload.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonDownload.Font = new System.Drawing.Font("Microsoft YaHei UI", 11.25F);
            this.buttonDownload.Location = new System.Drawing.Point(264, 283);
            this.buttonDownload.Name = "buttonDownload";
            this.buttonDownload.Size = new System.Drawing.Size(107, 32);
            this.buttonDownload.TabIndex = 14;
            this.buttonDownload.Text = "Scarica";
            this.buttonDownload.UseVisualStyleBackColor = true;
            this.buttonDownload.Click += new System.EventHandler(this.buttonDownload_Click);
            // 
            // progressBar
            // 
            this.progressBar.Location = new System.Drawing.Point(165, 374);
            this.progressBar.Name = "progressBar";
            this.progressBar.Size = new System.Drawing.Size(317, 23);
            this.progressBar.TabIndex = 15;
            // 
            // FormDownloadFattura
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(668, 492);
            this.Controls.Add(this.progressBar);
            this.Controls.Add(this.buttonDownload);
            this.Controls.Add(this.textBoxIdicket);
            this.Controls.Add(this.label2);
            this.Name = "FormDownloadFattura";
            this.Text = "FormDownloadFattura";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBoxIdicket;
        private System.Windows.Forms.Button buttonDownload;
        private System.Windows.Forms.ProgressBar progressBar;
    }
}