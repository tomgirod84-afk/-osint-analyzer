import asyncio
import edge_tts
import json
import os

VOICE = "fr-FR-HenriNeural"
OUT = os.path.join(os.path.dirname(__file__), "tiktok_voices")

os.makedirs(OUT, exist_ok=True)

lines = [
    {"id": "tk1", "text": "Tu savais que ninety three pour cent des mots de passe sont crackés en moins de six heures ?"},
    {"id": "tk2", "text": "Chaque caméra de surveillance autour de toi, est un port d'entrée."},
    {"id": "tk3", "text": "Ton téléphone te track, toutes les trente secondes."},
    {"id": "tk4", "text": "Le WiFi public, c'est comme pisser dans la piscine. Tout le monde est impacté."},
    {"id": "tk5", "text": "Un hacker ne casse pas la porte. Il te demande gentiment de l'ouvrir."},
    {"id": "tk6", "text": "Ta smart TV, t'écoute même éteinte."},
    {"id": "tk7", "text": "Quatre vingt dix huit pour cent des gens, utilisent le même mot de passe partout."},
    {"id": "tk8", "text": "Le dark web, c'est pas un autre internet. C'est le même, sans filtre."},
    {"id": "tk9", "text": "Un SIM swap, et ton compte Instagram, c'est à moi."},
    {"id": "tk10", "text": "Le phishing, c'est pas de la magie. C'est de la psychologie."},
    {"id": "tk11", "text": "Ton IP, c'est ton adresse postale, sur internet."},
    {"id": "tk12", "text": "Les mots de passe, c'est mort. Passe au passkey."},
    {"id": "tk13", "text": "Un hacker voit, ce que tu ne vois pas. Les failles, les portes, les faiblesses."},
    {"id": "tk14", "text": "Cybersécurité, c'est pas un métier. C'est un état d'esprit."},
    {"id": "tk15", "text": "Tout ce qui est connecté, peut être compromis. Tout."},
]

async def gen_one(line):
    comm = edge_tts.Communicate(line["text"], VOICE, rate="-5%", pitch="-2Hz")
    path = os.path.join(OUT, f"{line['id']}.mp3")
    await comm.save(path)
    print(f"  {line['id']}.mp3 OK")

async def main():
    for l in lines:
        await gen_one(l)
    manifest = {l["id"]: f"{l['id']}.mp3" for l in lines}
    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\n{len(lines)} voix regénérées (plus lentes, plus profondes)")

asyncio.run(main())
