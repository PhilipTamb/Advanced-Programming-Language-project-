using System.Threading.Tasks;
using System.Net.Http;
using System.Diagnostics;



namespace ClientUtenteCS
{
    internal class Richieste
    {

        public string HttpGet(string uri)
        {
            string content = null;

            var wc = new System.Net.WebClient();
            content = wc.DownloadString(uri);

            return content;
        }

        public async Task<string> HttpGetAsync(string uri)
        {
            string content = null;

            var client = new HttpClient();
            var response = await client.GetAsync(uri);
            if (response.IsSuccessStatusCode)
            {
                content = await response.Content.ReadAsStringAsync();
                Debug.WriteLine(content);
            }

          
            return content;
        }

        public async Task<string> HttpPostAsync(string uri, HttpContent cont)
        {
            string content = null;
            var client = new HttpClient();
            var response = await client.PostAsync(uri, cont);
            if (response.IsSuccessStatusCode)
            {
                content = await response.Content.ReadAsStringAsync();
                Debug.WriteLine(content);
            }
            return content;
        }

        
    }

    
}

