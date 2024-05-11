### Contexto

No meu projeto, qualquer pessoa que tenha informações sobre o solo e o clima de uma determinada região pode utilizar a plataforma para descobrir quais culturas são mais adequadas para serem cultivadas nesse ambiente.

Os usuários criam um perfil e fornecem os dados de solo e clima da região em questão.

Ao criar a consulta, os usuários podem incluir uma variedade de informações, como tipo de solo, nível de precipitação, temperatura média, pH do solo e outras características relevantes. Quanto mais detalhadas forem as informações fornecidas, mais precisas serão as recomendações feitas pela plataforma.

Em resumo, o projeto oferece uma plataforma intuitiva e personalizável para ajudar os agricultores, jardineiros e outros interessados em agricultura

### Objetivo

Construir um modelo de previsão de cultura para cultivo em uma determinada região

### O que temos disponível, inspirações e créditos

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset?resource=download

Elas estão disponíveis para download abaixo da aula (se você puxar os dados direto do Kaggle pode ser que encontre resultados diferentes dos meus, afinal as bases de dados podem ter sido atualizadas).

Caso queira uma outra solução, podemos olhar como referência a solução do usuário renjiabarai do kaggle no Notebook: https://www.kaggle.com/code/renjiabarai/crop-recommendation-prediction
Você vai perceber semelhanças entre a solução que vamos desenvolver aqui e a dele, mas também algumas diferenças significativas no processo de construção do projeto.

### Tecnologias utilizadas

**Pandas:** Para tratamento e analise exploratória de dados

**matplotlib - seaborn - plotly:** Para a criação de gráficos e analise de Outliers

**sklearn:** Biblioteca python utilizada para trabalhar com ML

**joblib:** Utilizado para armazenar o modelo ja treinado, assim podemos reutilizalo em outros projetos e ferramentas

**tkinter:** Biblioteca utilizada para deploy do projeto e criação de interfaces gráficas

### Parâmetros utilizados para avaliar os modelos

**1. Accuracy (Acurácia):** A proporção de exemplos classificados corretamente em relação ao total de exemplos.

**2. Precision (Precisão):** A proporção de exemplos positivos que foram classificados corretamente como positivos em relação a todos os exemplos classificados como positivos.

**3. Recall (Revocação):** A proporção de exemplos positivos que foram classificados corretamente como positivos em relação a todos os exemplos que são realmente positivos.

**4. F1-Score:** A média harmônica entre precisão e revocação. É útil quando há um desequilíbrio entre as classes.
