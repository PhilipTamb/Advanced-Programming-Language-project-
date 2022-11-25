# Advanced-Programming-Language-project-

InstaFix project for APL made by Vincenzo PLUCHINO & Philip TAMBE'
https://github.com/vinz97/InstaFix

##ISTRUZIONI PER ESEGUIRE IL CODICE

ATTENZIONE: Le istruzioni sul client in C# sono state testate e verificate su ambiente Windows
Su SO diversi come Mac o Linux potrebbero non funzionare


--- CLIENT C# --- 
Si consiglia di eseguire il codice su Microsoft Visual Studio (non Visual Studio Code)
In altri ambienti o IDE potrebbero sorgere dei problemi per la GUI dei Windows Forms
La cartella da scaricare da Github è "ClientUtenteCS" e il file "ClientUtenteCS.sln"
L'unico accorgimento è installare la libreria Newtonsoft. Per farlo, si osservino i seguenti passi:
--> su Visual Studio 2022, andare in alto nella voce PROGETTO (si trova in mezzo tra GIT e Compilazione)
--> cliccare sulla terzultima voce GESTISCI PACCHETTI NUGET...
--> cercare sulla barra di ricerca NETWONSOFT e cliccare per l'installazione automatica



--- SERVER GO --- 
L'IDE consigliato è GoLand di JetBrains.
Le folder da scaricare da Github sono "ServerGolang" e ".idea"
Per una corretta esecuzione innanzitutto è necessario cambiare in alto a destra su GoLand
le configurazioni di Run/Debug (la stringa accanto ai pulsanti verdi di run e debug): deve essere impostata su "go build *.go"
Riguardo le librerie da installare, si visiti la pagina https://github.com/go-sql-driver/mysql
alla voce installation è indicata la riga di comando da eseguire
N.B. è necessario avere GIT installato 


--- CLIENT PYTHON ---

per poter avviare il client python è necessario installare le librerie utilizzate nel codice, di seguito sono riportate i comandi del package installer pip:
pip install requests 
pip install tk 
pip install pyttk 
pip install Pillow 
pip install random 
pip install fpdf
a questo punto è possibile recarsi nella cartella del client python e lanciarlo attraverso il comando: python3 app.py questo perchè app.py conterrà il main

Se si utlizza Linux, i seguenti comandi sono utili per avviare Apache e SQL:
sudo systemctl start apache2
sudo service apache2 start
sudo systemctl enable apache2
start di mysql: mysql -u root -p



ALTRI ISTRUZIONI IMPORTANTI SUL SERVER

Per qualsiasi SO, se necessario bisogna modificare la riga 48 del file DATABASEMANAGEMENT.GO della funzione startDB inserendo le giuste credenziali per accedere a sql, l'host e la porta --> "user:password@tcp(localhost:3306)/instafix"
ATTENZIONE: il db deve essere già creato (anche senza tabelle) e il nome deve essere inserito sempre nella suddetta riga dopo lo /. 

Su Windows: sul file ServerManagement.go alla riga 302 della funzione uploadfile indicare il path di una cartella chiamata "fatture" (da creare se non esiste) che
deve essere inserita dentro htdocs di xamp (tipicamente si trova in C:\xamp\htdocs)

Su Linux: sempre sullo stesso file stessa riga, inserire solamente "../fatture" come path. La cartella in questo caso dovrà essere creata nel percorso /var/www/html
che è il path standard di Apache su Linux. In questo stesso percorso dovranno anche trovarsi tutti i file .go del server e runnare quindi da questo punto

a questo punto sia per anbiente Windows che per Linux è possibile recarsi nella cartella del client python e lanciarlo attraverso il comando:
python3 app.py 
questo perchè app.py conterrà il main

per quanto riguarda il server Go questo dovrà essere posizionato all'interno del server apache e quindi al path C:\xampp\htdocs\  per i terminali windows e nell'analogo path /var/www/html/ per terminali linux.
Al path sopraindicato oltre alla directory ServerGolang dovrà essere creata una cartella fatture per permetter al server di salvarsi i file pdf.

Al primo lancio del codice è necessario creare il db di nome instafix in mysql lasciandolo vuoto, sarè lo stesso server Go a chiedervi se volete popolare il DB con le tabelle perchè è la prima esecuzione e se volete avviarlo passando questo passaggio.

Inoltre all'esecuzione di Golang potrebbero verificarsi degli errori dovuti alle variabili dell'ambiente di esecuzione, è quindi necessario lanciare dal terminale del server i seguenti comandi:
go env -w GO111MODULE=auto
go env -w GO111MODULE=off
go get -u github.com/go-sql-driver/mysql

quindi per compilare i file del server lanciare 
go build
e poi per eseguire
go run .

