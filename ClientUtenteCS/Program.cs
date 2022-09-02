using System;
using System.Windows.Forms;


namespace ClientUtenteCS
{
    internal static class Program
    {
        /// <summary>
        /// Punto di ingresso principale dell'applicazione (main)
        /// </summary>
        [STAThread]
        static void Main()
        {
         Application.EnableVisualStyles();
         Application.SetCompatibleTextRenderingDefault(false);
         Application.Run(new FormLogin());
        }

    }
}
