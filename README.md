# Mihon Extensions (no NSFW)

Este é um *fork* **filtrado** do repositório de extensões do Keiyoushi, com exclusao de conteúdos específicos (como listado na lógica do *workflow*).

**⚠️ Aviso:** Esta é uma fonte de extensões **não oficial e modificada**.

---

## 🚀 Como Usar este Repositório Filtrado

**O uso desta fonte é de sua total responsabilidade, pois ela não é a fonte oficial.**

Você pode adicionar o repositório **modificado** no seu aplicativo usando a URL direta:

* **URL do Conteudo Filtrado:**
    ```
    https://cdn.jsdelivr.net/gh/MiguelMA3/mihon-extensions@mypack/index.min.json
    ```

### 📝 Guia

1. No aplicativo Mihon, acesse **Navegar**>**Extensoes**
2. No canto superior direito clique no **menu**>**Repositorio de extensoes**
3. Clique em **Adicionar** e cole a URL acima.

---

## 🗑️ Filtros Aplicados

Este repositório passa por um processo automatizado (via GitHub Actions) que remove extensões listadas em `PKG_REMOVE_LIST` antes de gerar os arquivos `index.json` e `index.min.json`.

* **Conteúdo Removido:** Conteúdo listado no arquivo `filter_extensions.py` (Principalmente conteúdo NSFW, conforme configurado).

---

## 🔗 Links de Referência

Para documentação oficial, código-fonte e relatórios de problemas sobre as extensões originais:

* **Guia de Introdução (Original):** Leia o [Guia de Introdução da Keiyoushi](https://keiyoushi.github.io/docs/guides/getting-started#adding-the-extension-repo) se você for novo no sistema.
* **Source Code (Original):** https://github.com/keiyoushi/extensions-source
* **Reportar Issues (Original):** https://github.com/keiyoushi/extensions-source/issues/new/choose

---

## 🛠️ Outras Opções (Apenas se Não Usar o Fork)

Se você não estiver usando este *fork* filtrado, você pode baixar e atualizar as extensões manualmente a partir da [página de listagem oficial](https://keiyoushi.github.io/extensions/).
