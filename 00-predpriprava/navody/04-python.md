# Python pro výpočty a technický balíček

Použijte Python 3.10 nebo novější z [python.org](https://www.python.org/downloads/). Na Windows ověřte `py -3 --version` nebo `python --version`; na macOS/Linux `python3 --version`. Všechny další příkazy musí používat tentýž interpreter.

V **kořenu celého repozitáře**, kde je `requirements-dev.txt`, založte vlastní prostředí:

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest --version
```

Pokud nemáte příkaz `py`, první řádek proveďte přes `python -m venv .venv`.

macOS/Linux:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements-dev.txt
./.venv/bin/python -m pytest --version
```

Ve VS Code vyberte tento interpreter (Python: Select Interpreter). V novém terminálu ověřte `python -c "import sys; print(sys.executable)"` a `python -m pytest --version`. Pokud automatická aktivace nefunguje, používejte plnou cestu k `.venv` interpreteru. Pytest je potřeba pro technickou větev; PyYAML slouží ke kontrole konfigurací materiálů.

Příkazy v úlohách používají `python` jako označení ověřeného interpreteru. `python -m pytest` neinstaluje pytest; pokud modul chybí, vraťte se k instalaci závislostí.

Při technických cvičeních spouštějte program a testy z `balicek-technicke/projekt/znamkovy-kalkulator/`. Otevřeným workspace nadále zůstává celý balíček.
