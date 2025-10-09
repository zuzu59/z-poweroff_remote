# z-poweroff_remote
Petit serveur web tout simple avec un bouton pour éteindre une machine à distance

zf250824.1755, zf251009.1708

ATTENTION: tous mes trucs tournent dans /root/dev dans mes containers LXC sous Proxmox.<br>
Il faudra donc modifier les 'racines' des scripts en conséquence !


## Installation
```
mkdir -p /root/dev
cd /root/dev
git clone git@github.com:zuzu59/z-poweroff_remote.git
```


## Utilisation depuis une console
```
python3 /root/dev/z-poweroff_remote/poweroff_web.py
```

## Utilisation depuis le crontab
```
crontab -e
```

et ajouter cette ligne

```
@reboot /usr/bin/python3 /root/dev/z-poweroff_remote/poweroff_web.py > /root/sortie.log 2> /root/z-poweroff_remote-erreurs.log &
```


## Pour arrêter la machine depuis l'interface WEB
http://adrsip_machine:1859


## Sources: demandé à Ollama qwen3:4b ;-)
