# z-poweroff_remote
Petit serveur web tout simple avec un bouton pour éteindre une machine à distance

zf250824.1755, zf251005.1220


## Installation
git clone git@github.com:zuzu59/z-poweroff_remote.git


## Utilisation depuis une console
python3 /root/z-poweroff_remote/poweroff_web.py


## Utilisation depuis le crontab
ATTENTION: il faut faire le git clone dans le dossier /root !

crontab -e

et ajouter cette ligne

@reboot /usr/bin/python3 /root/z-poweroff_remote/poweroff_web.py > /root/sortie.log 2> /root/erreurs.log &


## Pour arrêter la machine

http://adrsip_machine:1859


## Sources: demandé à Ollama qwen3:4b ;-)


