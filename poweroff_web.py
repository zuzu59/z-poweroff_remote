# zf250824.1731
# web_poweroff_server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import subprocess
import threading
import urllib.parse

# Configuration
PORT = 1859
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Power Off</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        button {
            padding: 20px 40px;
            font-size: 24px;
            font-weight: bold;
            background-color: #ff4d4d;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #e03a3a;
        }
    </style>
</head>
<body>
    <button onclick="window.location.href='/poweroff'">Power OFF</button>
</body>
</html>
"""

class PowerOffHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode())
        elif self.path == '/poweroff':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Powering off the system...</h1>")
            # Exécuter poweroff en arrière-plan
            threading.Thread(target=self.execute_poweroff, daemon=True).start()
            # Renvoyer une page de confirmation
            self.wfile.write(b"<p>Power off command sent. System will shut down.</p>")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")

    def execute_poweroff(self):
        try:
            # Exécute la commande poweroff
            print("Envoi de la commande poweroff...")
            subprocess.run(['/usr/sbin/poweroff'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de poweroff : {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

def run_server():
    try:
        server_address = ('', PORT)
        httpd = HTTPServer(server_address, PowerOffHandler)
        print(f"Serveur web démarré sur http://localhost:{PORT}")
        print("Accédez à http://<votre_ip_locale>:1859 depuis un autre ordinateur.")
        print("Exemple : http://192.168.1.10:1859")
        httpd.serve_forever()
    except Exception as e:
        print(f"Erreur lors du démarrage du serveur : {e}")

if __name__ == "__main__":
    run_server()

