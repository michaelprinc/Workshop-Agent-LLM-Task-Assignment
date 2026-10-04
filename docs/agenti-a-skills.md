# Projektové pokyny, vlastní agenti a skills

Nejdříve otevřete celou složku jednoho balíčku ve VS Code. `.github/` musí být v kořenu otevřeného workspace. Zkontrolujte zvolený harness a jeho podporu těchto formátů.

- `.github/copilot-instructions.md`: průběžná pravidla projektu.
- `.github/instructions/*.instructions.md`: pokyny pro vybrané soubory s `applyTo`.
- `.github/agents/*.agent.md`: role, dostupné nástroje a případné handoffy.
- `.github/skills/<nazev>/SKILL.md`: postup načítaný při relevantním úkolu; `name` musí odpovídat názvu složky.

## Ověření načtení

1. V nastavení přizpůsobení chatu nebo diagnostice zkontrolujte skutečně načtené pokyny a jejich cestu.
2. Vlastního agenta vyberte v nabídce agentů. Nespoléhejte na to, že libovolné `@jmeno` vybere vaši roli.
3. Zkontrolujte seznam dostupných nástrojů. Jejich názvy a dostupnost se mohou mezi harnessy lišit; chybějící nástroj se nemusí načíst.
4. Skills vyhledejte v přizpůsobení chatu, příkazem `/skills` nebo v nabídce `/` podle své verze. Dostupnost skillu nezaručuje jeho použití při každém promptu.
5. Po změně konfigurace ověřte načtení znovu v novém chatu; pokud se seznam neaktualizuje, znovu načtěte okno. Nepovažujte restart za náhradu kontroly konfigurace.

Pokud potřebujete nápovědu k formátu, použijte [prázdné šablony](../sablony/konfigurace.md); neobsahují specifickou roli ani hotový postup cvičení.

## Delegace

V Local harnessu ověřte nástroj `agent/runSubagent`. Koordinátor s vlastním seznamem nástrojů musí mít sadu nástrojů `agent`; seznam `agents` může navíc omezit dostupné role. V jiném harnessu ověřte odpovídající schopnost podle dokumentace. Samostatné bloky v odpovědi samy nedokazují spuštění subagentů nebo paralelní běh.

Každému podúkolu předejte cíl, relevantní vstupy, omezení a požadovaný výstup. Nezávislé zápisy musí mít různé cílové soubory. Pokud delegace není dostupná, použijte oddělené chaty a ruční předání; v záznamu označte, že šlo o alternativu.

[Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents) · [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) · [Subagents](https://code.visualstudio.com/docs/agents/run/subagents) · [Nástroje](https://code.visualstudio.com/docs/agents/reference/tools-reference)
