# Case Técnico Sparta

## Desafio:
Crie um sistema que persista informações sobre companhias abertas em um banco de dados e permita consultar essas informações posteriormente. Note que esses dados podem mudar de uma data para outra (DENOM_SOCIAL e SIT) e que o usuário gostaria de acessar informações para uma determinada data.

### Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

- **Python 3.12**
  - [Download Python](https://www.python.org/downloads/)
- **Pip** (gerenciador de pacotes do Python)
  - Instalação: `python -m ensurepip --upgrade`
- **Flask 3.0.3**
  - Instalação: `pip install flask==3.0.3`
- **Numpy 1.26.2**
  - Instalação: `pip install numpy==1.26.2`
- **Pandas 2.2.2**
  - Instalação: `pip install pandas==2.2.2`
- **Bootstrap** (utilizado no HTML)
  - Adicionado via CDN (nenhuma instalação adicional necessária)



### Instalação

- Clone o repositório:
  - `git clone https://github.com/seu_usuario/seu_projeto.git`

### Como rodar o arquivo

- Inicialize o arquivo **main.py**
  - `python main.py`

- Abra seu navegador na URL http://127.0.0.1:5000 caso você não tenha mudado a porta padrão do Flask.

### Como usar

1. Na barra de busca, digite o `DENOM_SOCIAL` que deseja procurar e clique no botão "Procurar".
2. Alternativamente, você pode usar o dropdown para escolher uma categoria de `SIT` e clicar no botão "Procurar".
3. Você também pode combinar as duas opções: digite o `DENOM_SOCIAL`, escolha uma categoria de `SIT` no dropdown e clique no botão "Procurar".

# Etapas do Projeto
### 1. Análise e Processamento do Arquivo CSV

Comecei o projeto baixando o arquivo que me pediram e fiz uma análise do conteúdo usando métodos do pandas. Carreguei o arquivo CSV, identifiquei as colunas que não eram necessárias e as removi, mantendo apenas as colunas de interesse. Em seguida, armazenei os dados resultantes em uma nova variável. Por fim, converti o DataFrame resultante em um novo arquivo CSV.

### 2. Integração com Banco de Dados SQLite

Após isso, quis integrar esse arquivo CSV em um banco de dados e resolvi utilizar o SQLite, já que ele vem instalado nos pacotes do Python. Criei uma função chamada processar_csv_para_sqlite, que tem como objetivo:

- Estabelecer uma conexão com o banco de dados
- Criar a tabela necessária para consulta
- Ler os dados do arquivo CSV
- Inserir esses dados na tabela
- Também tratei os erros para garantir que o algoritmo não pare de - funcionar em caso de problemas.

### 3. Aplicação Web com Flask

Para facilitar a consulta ao banco de dados, criei uma aplicação Flask que integra a tabela criada pela função processar_csv_para_sqlite através de um formulário web. A aplicação permite que os usuários consultem os dados usando critérios de busca e filtros, exibindo os resultados em um template HTML. A aplicação trata tanto requisições GET quanto POST para processar as buscas e exibir os dados filtrados.

### 4. Design com Bootstrap

Para melhorar o design da aplicação web, utilizei o Bootstrap, um popular framework CSS. Isso proporciona um layout responsivo e visualmente agradável.
