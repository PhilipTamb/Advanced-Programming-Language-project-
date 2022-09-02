namespace ClientUtenteCS
{
    partial class FormHomepage
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
            this.panelMenu = new System.Windows.Forms.Panel();
            this.panelLogo = new System.Windows.Forms.Panel();
            this.buttonTicketAdd = new System.Windows.Forms.Button();
            this.panelTitle = new System.Windows.Forms.Panel();
            this.buttonExit = new System.Windows.Forms.Button();
            this.labelTitle = new System.Windows.Forms.Label();
            this.panelSottostante = new System.Windows.Forms.Panel();
            this.buttonBackHome = new System.Windows.Forms.Button();
            this.buttonReview = new System.Windows.Forms.Button();
            this.buttonFatture = new System.Windows.Forms.Button();
            this.buttonPreventivi = new System.Windows.Forms.Button();
            this.buttonViewTicket = new System.Windows.Forms.Button();
            this.buttonAddTicket = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.panelMenu.SuspendLayout();
            this.panelLogo.SuspendLayout();
            this.panelTitle.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // panelMenu
            // 
            this.panelMenu.BackColor = System.Drawing.Color.Firebrick;
            this.panelMenu.Controls.Add(this.buttonReview);
            this.panelMenu.Controls.Add(this.buttonFatture);
            this.panelMenu.Controls.Add(this.buttonPreventivi);
            this.panelMenu.Controls.Add(this.buttonViewTicket);
            this.panelMenu.Controls.Add(this.buttonAddTicket);
            this.panelMenu.Controls.Add(this.panelLogo);
            this.panelMenu.Dock = System.Windows.Forms.DockStyle.Left;
            this.panelMenu.Location = new System.Drawing.Point(0, 0);
            this.panelMenu.Name = "panelMenu";
            this.panelMenu.Size = new System.Drawing.Size(200, 611);
            this.panelMenu.TabIndex = 0;
            // 
            // panelLogo
            // 
            this.panelLogo.BackColor = System.Drawing.Color.LightCoral;
            this.panelLogo.Controls.Add(this.pictureBox1);
            this.panelLogo.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelLogo.Location = new System.Drawing.Point(0, 0);
            this.panelLogo.Name = "panelLogo";
            this.panelLogo.Size = new System.Drawing.Size(200, 80);
            this.panelLogo.TabIndex = 0;
            // 
            // buttonTicketAdd
            // 
            this.buttonTicketAdd.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonTicketAdd.FlatAppearance.BorderSize = 0;
            this.buttonTicketAdd.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonTicketAdd.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.buttonTicketAdd.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonTicketAdd.Location = new System.Drawing.Point(0, 80);
            this.buttonTicketAdd.Name = "buttonTicketAdd";
            this.buttonTicketAdd.Size = new System.Drawing.Size(200, 60);
            this.buttonTicketAdd.TabIndex = 0;
            this.buttonTicketAdd.Text = "Crea un ticket";
            this.buttonTicketAdd.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonTicketAdd.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.buttonTicketAdd.UseVisualStyleBackColor = true;
            // 
            // panelTitle
            // 
            this.panelTitle.BackColor = System.Drawing.Color.Maroon;
            this.panelTitle.Controls.Add(this.buttonExit);
            this.panelTitle.Controls.Add(this.buttonBackHome);
            this.panelTitle.Controls.Add(this.labelTitle);
            this.panelTitle.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelTitle.Location = new System.Drawing.Point(200, 0);
            this.panelTitle.Name = "panelTitle";
            this.panelTitle.Size = new System.Drawing.Size(684, 80);
            this.panelTitle.TabIndex = 1;
            // 
            // buttonExit
            // 
            this.buttonExit.BackColor = System.Drawing.Color.Firebrick;
            this.buttonExit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonExit.FlatAppearance.BorderSize = 0;
            this.buttonExit.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonExit.Font = new System.Drawing.Font("Ebrima", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonExit.ForeColor = System.Drawing.Color.White;
            this.buttonExit.Location = new System.Drawing.Point(656, 0);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(28, 30);
            this.buttonExit.TabIndex = 21;
            this.buttonExit.Text = "x";
            this.buttonExit.TextAlign = System.Drawing.ContentAlignment.TopRight;
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Microsoft YaHei", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelTitle.ForeColor = System.Drawing.Color.White;
            this.labelTitle.Location = new System.Drawing.Point(249, 23);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(204, 28);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "Benvenuto, utente!";
            // 
            // panelSottostante
            // 
            this.panelSottostante.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelSottostante.Location = new System.Drawing.Point(200, 80);
            this.panelSottostante.Name = "panelSottostante";
            this.panelSottostante.Size = new System.Drawing.Size(684, 531);
            this.panelSottostante.TabIndex = 2;
            // 
            // buttonBackHome
            // 
            this.buttonBackHome.Dock = System.Windows.Forms.DockStyle.Left;
            this.buttonBackHome.FlatAppearance.BorderSize = 0;
            this.buttonBackHome.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonBackHome.Image = global::ClientUtenteCS.Properties.Resources.home_icon;
            this.buttonBackHome.Location = new System.Drawing.Point(0, 0);
            this.buttonBackHome.Name = "buttonBackHome";
            this.buttonBackHome.Size = new System.Drawing.Size(75, 80);
            this.buttonBackHome.TabIndex = 3;
            this.buttonBackHome.UseVisualStyleBackColor = true;
            this.buttonBackHome.Click += new System.EventHandler(this.buttonBackHome_Click);
            // 
            // buttonReview
            // 
            this.buttonReview.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonReview.FlatAppearance.BorderSize = 0;
            this.buttonReview.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonReview.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonReview.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.buttonReview.Image = global::ClientUtenteCS.Properties.Resources.recensione_img;
            this.buttonReview.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonReview.Location = new System.Drawing.Point(0, 320);
            this.buttonReview.Name = "buttonReview";
            this.buttonReview.Padding = new System.Windows.Forms.Padding(12, 0, 0, 0);
            this.buttonReview.Size = new System.Drawing.Size(200, 60);
            this.buttonReview.TabIndex = 4;
            this.buttonReview.Text = "  Recensioni";
            this.buttonReview.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonReview.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.buttonReview.UseVisualStyleBackColor = true;
            this.buttonReview.Click += new System.EventHandler(this.buttonReview_Click);
            // 
            // buttonFatture
            // 
            this.buttonFatture.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonFatture.FlatAppearance.BorderSize = 0;
            this.buttonFatture.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonFatture.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.buttonFatture.Image = global::ClientUtenteCS.Properties.Resources.ricevuta_img;
            this.buttonFatture.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonFatture.Location = new System.Drawing.Point(0, 260);
            this.buttonFatture.Name = "buttonFatture";
            this.buttonFatture.Padding = new System.Windows.Forms.Padding(12, 0, 0, 0);
            this.buttonFatture.Size = new System.Drawing.Size(200, 60);
            this.buttonFatture.TabIndex = 3;
            this.buttonFatture.Text = "   Fatture";
            this.buttonFatture.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonFatture.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.buttonFatture.UseVisualStyleBackColor = true;
            this.buttonFatture.Click += new System.EventHandler(this.buttonFatture_Click);
            // 
            // buttonPreventivi
            // 
            this.buttonPreventivi.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonPreventivi.FlatAppearance.BorderSize = 0;
            this.buttonPreventivi.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonPreventivi.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.buttonPreventivi.Image = global::ClientUtenteCS.Properties.Resources.preventivo_img;
            this.buttonPreventivi.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonPreventivi.Location = new System.Drawing.Point(0, 200);
            this.buttonPreventivi.Name = "buttonPreventivi";
            this.buttonPreventivi.Padding = new System.Windows.Forms.Padding(12, 0, 0, 0);
            this.buttonPreventivi.Size = new System.Drawing.Size(200, 60);
            this.buttonPreventivi.TabIndex = 2;
            this.buttonPreventivi.Text = "Preventivi";
            this.buttonPreventivi.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonPreventivi.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.buttonPreventivi.UseVisualStyleBackColor = true;
            this.buttonPreventivi.Click += new System.EventHandler(this.buttonPreventivi_Click);
            // 
            // buttonViewTicket
            // 
            this.buttonViewTicket.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonViewTicket.FlatAppearance.BorderSize = 0;
            this.buttonViewTicket.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonViewTicket.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.buttonViewTicket.Image = global::ClientUtenteCS.Properties.Resources.elenco_img;
            this.buttonViewTicket.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonViewTicket.Location = new System.Drawing.Point(0, 140);
            this.buttonViewTicket.Name = "buttonViewTicket";
            this.buttonViewTicket.Padding = new System.Windows.Forms.Padding(12, 0, 0, 0);
            this.buttonViewTicket.Size = new System.Drawing.Size(200, 60);
            this.buttonViewTicket.TabIndex = 1;
            this.buttonViewTicket.Text = "     Visualizza ticket";
            this.buttonViewTicket.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonViewTicket.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.buttonViewTicket.UseVisualStyleBackColor = true;
            this.buttonViewTicket.Click += new System.EventHandler(this.buttonViewTicket_Click);
            // 
            // buttonAddTicket
            // 
            this.buttonAddTicket.Dock = System.Windows.Forms.DockStyle.Top;
            this.buttonAddTicket.FlatAppearance.BorderSize = 0;
            this.buttonAddTicket.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonAddTicket.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.buttonAddTicket.Image = global::ClientUtenteCS.Properties.Resources.plus_img;
            this.buttonAddTicket.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonAddTicket.Location = new System.Drawing.Point(0, 80);
            this.buttonAddTicket.Name = "buttonAddTicket";
            this.buttonAddTicket.Padding = new System.Windows.Forms.Padding(12, 0, 0, 0);
            this.buttonAddTicket.Size = new System.Drawing.Size(200, 60);
            this.buttonAddTicket.TabIndex = 0;
            this.buttonAddTicket.Text = "  Crea ticket";
            this.buttonAddTicket.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.buttonAddTicket.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageBeforeText;
            this.buttonAddTicket.UseVisualStyleBackColor = true;
            this.buttonAddTicket.Click += new System.EventHandler(this.buttonAddTicket_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::ClientUtenteCS.Properties.Resources.output_onlinepngtools;
            this.pictureBox1.Location = new System.Drawing.Point(47, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(90, 77);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // FormHomepage
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(884, 611);
            this.Controls.Add(this.panelSottostante);
            this.Controls.Add(this.panelTitle);
            this.Controls.Add(this.panelMenu);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "FormHomepage";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "FormHomepage";
            this.panelMenu.ResumeLayout(false);
            this.panelLogo.ResumeLayout(false);
            this.panelTitle.ResumeLayout(false);
            this.panelTitle.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panelMenu;
        private System.Windows.Forms.Button buttonAddTicket;
        private System.Windows.Forms.Panel panelLogo;
        private System.Windows.Forms.Button buttonReview;
        private System.Windows.Forms.Button buttonFatture;
        private System.Windows.Forms.Button buttonPreventivi;
        private System.Windows.Forms.Button buttonViewTicket;
        private System.Windows.Forms.Button buttonTicketAdd;
        private System.Windows.Forms.Panel panelTitle;
        private System.Windows.Forms.Label labelTitle;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Panel panelSottostante;
        private System.Windows.Forms.Button buttonBackHome;
        private System.Windows.Forms.Button buttonExit;
    }
}