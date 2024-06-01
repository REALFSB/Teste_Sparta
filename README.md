# Etapas do Projeto
## **1. Análise e Processamento do Arquivo CSV**

Comecei o projeto baixando o arquivo que me pediram e fiz uma análise do conteúdo usando métodos do pandas. Carreguei o arquivo CSV, identifiquei as colunas que não eram necessárias e as removi, mantendo apenas as colunas de interesse. Em seguida, armazenei os dados resultantes em uma nova variável. Por fim, converti o DataFrame resultante em um novo arquivo CSV.

## **2. Integração com Banco de Dados SQLite**

Após isso, quis integrar esse arquivo CSV em um banco de dados e resolvi utilizar o SQLite, já que ele vem instalado nos pacotes do Python. Criei uma função chamada processar_csv_para_sqlite, que tem como objetivo:

- Estabelecer uma conexão com o banco de dados
- Criar a tabela necessária para consulta
- Ler os dados do arquivo CSV
- Inserir esses dados na tabela
- Também tratei os erros para garantir que o algoritmo não pare de - funcionar em caso de problemas.

## **3. Aplicação Web com Flask**

Para facilitar a consulta ao banco de dados, criei uma aplicação Flask que integra a tabela criada pela função processar_csv_para_sqlite através de um formulário web. A aplicação permite que os usuários consultem os dados usando critérios de busca e filtros, exibindo os resultados em um template HTML. A aplicação trata tanto requisições GET quanto POST para processar as buscas e exibir os dados filtrados.

## **4. Design com Bootstrap**

Para melhorar o design da aplicação web, utilizei o Bootstrap, um popular framework CSS. Isso proporciona um layout responsivo e visualmente agradável.
