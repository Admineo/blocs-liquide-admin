#!/usr/bin/env python3
"""Construit les deux versions du jeu à partir de source/blocs.src.html
   - www/index.html        : version pour les stores (SANS menu caché, SANS photo intégrée)
   - blocs-perso.html : version personnelle (menu caché code 1140 + photo de fond)
Usage : python3 build.py
"""
import re,os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'source','blocs.src.html'),encoding='utf-8').read()

STORE_BG="""function refreshBg(){document.body.classList.toggle('hasbg',!!customBg);const s=document.body.style;
 if(customBg){s.setProperty('background-image','url("'+customBg+'")','important');}
 else{s.removeProperty('background-image');s.animation='none';s.backgroundImage=bgUrl(playLvl);s.backgroundSize='cover';s.backgroundPosition='center bottom';s.backgroundAttachment='fixed';s.backgroundRepeat='no-repeat';}
 $('bgclear').style.display=customBg?'':'none';}
"""
def strip(t,a,b):
    return re.sub(re.escape(a)+r'.*?'+re.escape(b),'',t,flags=re.S)

# --- adresse du fichier de réglages à distance (facultative) : remote/rc_url.txt
def read_rc_url():
    f=os.path.join(here,'remote','rc_url.txt')
    if not os.path.exists(f):return ''
    for line in open(f,encoding='utf-8'):
        line=line.strip()
        if line and not line.startswith('#'):
            assert line.startswith('https://') and '"' not in line and ' ' not in line,"rc_url.txt : une adresse https:// sans espace est attendue"
            return line
    return ''
RC_URL=read_rc_url()
src=src.replace('const RC_URL="";','const RC_URL="'+RC_URL+'";')

# --- version stores
st=src
for a,b in (("/*ADMIN-BEGIN*/","/*ADMIN-END*/"),("<!--ADMIN-BEGIN-->","<!--ADMIN-END-->")):
    st=strip(st,a,b)
st=re.sub(r'/\*PHOTO-BEGIN\*/.*?/\*PHOTO-END\*/',lambda m:STORE_BG,st,flags=re.S)
for bad in ('openAdmin','secretTap','admSync','PHOTO','1140','pinHash','id="admin"'):
    assert bad not in st,("reste dans la version stores :",bad)
os.makedirs(os.path.join(here,'www'),exist_ok=True)
open(os.path.join(here,'www','index.html'),'w',encoding='utf-8').write(st)

# --- version perso
pe=src
for m in ("/*ADMIN-BEGIN*/","/*ADMIN-END*/","<!--ADMIN-BEGIN-->","<!--ADMIN-END-->","/*PHOTO-BEGIN*/","/*PHOTO-END*/"):
    pe=pe.replace(m,"")
pass
open(os.path.join(here,'blocs-perso.html'),'w',encoding='utf-8').write(pe)
print("Réglages à distance :",RC_URL or "désactivés (remote/rc_url.txt vide)");print("OK  stores:",len(st)//1024,"Ko  perso:",len(pe)//1024,"Ko")
