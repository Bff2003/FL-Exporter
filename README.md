# FL-Exporter

Ferramenta de linha de comandos para exportar automaticamente todos os  projetos do FL Studio (`.flp`) para o formato projeto zipados (`.zip`).

## Funcionalidades

- **Descoberta Automática**: Encontra automaticamente ficheiros `.flp` num diretório e nos seus subdiretórios.
- **Exportação em Lote**: Exporta múltiplos projetos de uma só vez.
- **Configurável**: Permite personalizar os caminhos para o executável do FL Studio, a pasta de projetos e o diretório de saída através de parâmetros de linha de comando.
- **Organização**: Move automaticamente os ficheiros `.zip` exportados para um diretório de destino especificado.
- **Flexível**: Ignora pastas comuns que não precisam de ser exportadas (como a pasta `Backup`).

## Instalação

1.  Clone este repositório:
    ```sh
    git clone https://github.com/Bff2003/FL-Exporter.git
    ```
2.  Entre no diretório do projeto:
    ```sh
    cd FL-Exporter
    ```

## Como Usar

O script é executado a partir do terminal e pode ser configurado através de argumentos de linha de comando.

### Uso Básico

Para executar o script com os caminhos padrão (geralmente funciona para uma instalação padrão do FL Studio no Windows), basta executar:

```sh
python main.py
```

### Uso Avançado

Você pode especificar caminhos personalizados para o executável do FL Studio, o diretório dos seus projetos e a pasta de saída.

```sh
python main.py --executable "C:\OutroCaminho\FL Studio 21\FL64.exe" --projects-dir "D:\Musica\Projetos" --output-dir "D:\Backups\FL"
```

### Argumentos da Linha de Comando

- `--executable`: (Opcional) Caminho completo para o executável `FL64.exe`. O padrão é `C:\Program Files\Image-Line\FL Studio 21\FL64.exe`.
- `--output-dir`: (Opcional) Diretório onde os ficheiros `.zip` exportados serão guardados. O padrão é `%UserProfile%\Documents\fl_exporter`.
- `--projects-dir`: (Opcional) Diretório onde o script irá procurar por ficheiros `.flp`. O padrão é `%UserProfile%\Documents\Image-Line\FL Studio\Projects`.