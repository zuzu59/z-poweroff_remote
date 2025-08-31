# z-poweroff_remote
Petit serveur web tout simple avec un bouton pour éteindre une machine à distance

zf250824.1755, zf250831.2305


## Utilisation depuis une console

python3 poweroff_web.py


## Utilisation depuis le crontab
ATTENTION: il faut faire le git clone dans le dossier /root !

crontab -e

et ajouter cette ligne

@reboot /usr/bin/python3 /root/z-poweroff_remote/poweroff_web.py > /root/sortie.log 2> /root/erreurs.log &


## Pour arrêter la machine

http://adrsip_machine:1859


## Sources: demandé à Ollama qwen3:4b ;-)


