# Advanced-Programming-Language-project-

per poter avviare il client python è necessario installare le librerie utilizzate nel codice, di seguito sono riportate i comandi del package installer pip:

pip install requests
pip install tk
pip install pyttk
pip install Pillow
pip install random
pip install fpdf

dopo averle installate è necessario lanciare il server apache e mysql 

comandi apache per linux:
sudo systemctl start apache2

sudo service apache2 start

sudo systemctl enable apache2

start di mysql:
mysql -u root -p

a questo punto è possibile recarsi nella cartella del client python e lanciarlo attraverso il comando:
python3 app.py 
questo perchè app.py conterrà il main

per quanto riguarda il server Go questo dovrà essere posizionato all'interno del server apache e quindi al path C:\xampp\htdocs\  per i terminali windows e nell'analogo path /var/www/html/ per terminali linux.
Al path sopraindicato oltre alla directory ServerGolang dovrà essere creata una cartella fatture per permetter al server di salvarsi i file pdf.
