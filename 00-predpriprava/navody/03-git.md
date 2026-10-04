# Git

Nainstalujte Git podle [oficiálního návodu](https://git-scm.com/install/) a v novém terminálu ověřte `git --version`.

Pro své commity nastavte jméno a e-mail. Veřejné commity mohou tyto údaje zveřejnit; můžete použít GitHub noreply adresu.

```bash
git config --global user.name "Moje jméno"
git config --global user.email "Moje adresa pro commity"
```

Pokračujte [návodem k vlastní větvi](../../docs/ucastnicka-vetev.md). Příkazy `git status`, `git diff` a historie commitů slouží k ověření změn. ZIP umožní práci se soubory, ale pro verzování jej rozbalte do nového adresáře a založte vlastní Git příkazem `git init -b main`; původní ZIP si ponechte jako čistý výchozí podklad.
