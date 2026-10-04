# Kontrola materiálů

Kontrola je určena především autorům distribuce. Nehodnotí správnost výsledků účastníka a nenahrazuje čtení obsahu člověkem.

Z kořene repozitáře, v připraveném prostředí:

```bash
python tools/validate_materials.py
```

Před publikací čistého výchozího podkladu použijte:

```bash
python tools/validate_materials.py --distribution --history
```

Kontrola ověřuje manifest zadání, povinné části úloh, relativní odkazy, YAML definice rolí a skills, nepřítomnost lektorských souborů a zachování vstupů. Distribuční režim navíc kontroluje prázdné výstupní složky a nepřítomnost předem dodaných konfigurací, které má vytvořit účastník. Kontrola historie prochází všechny lokálně dostupné commity dosažitelné z referencí; neověřuje cizí vzdálené repozitáře ani zbytky objektů z dříve použitého klonu.

Pokud modul `yaml` chybí, nainstalujte závislosti podle [předpřípravy](../00-predpriprava/navody/04-python.md).

Před vydáním projděte také obsah zadání, teorie, názvy a popisy agentů. Obecný skript nemůže spolehlivě poznat každou větu, která prozrazuje konkrétní výsledek. Novou distribuci vytvářejte z čistého adresáře, do její historie nepřidávejte lektorské odpovědi ani účastnické výstupy.
