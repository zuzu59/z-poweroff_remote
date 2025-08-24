# z-poweroff_remote
Petit serveur web tout simple avec un bouton pour éteindre une machine à distance

zf250824.1755


## Utilisation depuis une console:

python3 poweroff_web.py

## Utilisation depuis le crontab

crontab -e

et ajouter cette ligne

@reboot /usr/bin/python3 /root/z-poweroff_remote/poweroff_web.py > /root/sortie.log 2> /root/erreurs.log &


## Sources: demandé à Ollama qwen3:4b ;-)


