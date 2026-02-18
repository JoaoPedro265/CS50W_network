<img style="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=header&fontColor=FFFFFF&theme=cobalt" />

<h1 align="left">📱 Network - Rede Social (CS50W)</h1>

<p align="left">
Uma plataforma de rede social completa onde usuários podem interagir através de postagens, seguidores e curtidas. O projeto foca na criação de uma interface dinâmica que utiliza <strong>JavaScript assíncrono</strong> para permitir edições e interações sem recarregar a página.
</p>

###

<h2 align="left">🚀 Funcionalidades Principais</h2>

<ul>
  <li><strong>Feed Global e Personalizado:</strong> Visualização de todos os posts ou apenas de usuários que você segue.</li>
  <li><strong>Sistema de Seguidores:</strong> Lógica de "Follow/Unfollow" com contagem dinâmica no perfil do usuário.</li>
  <li><strong>Edição In-place (JS):</strong> Edição de postagens em tempo real usando JavaScript para substituir o conteúdo por um <code>textarea</code> sem <i>refresh</i>.</li>
  <li><strong>Likes Assíncronos:</strong> Curtir e descurtir posts com atualização imediata do contador via Fetch API.</li>
  <li><strong>Paginação:</strong> Navegação eficiente entre grandes volumes de posts (10 por página) utilizando o <code>Paginator</code> do Django.</li>
  <li><strong>Perfis Detalhados:</strong> Páginas de perfil que exibem estatísticas e histórico de postagens do usuário.</li>
</ul>

###

<h2 align="left">🛠️ Tecnologias Utilizadas</h2>

<div align="left">
  <img src="https://skillicons.dev/icons?i=py,django,js,html,css,sqlite,bootstrap" height="40" />
</div>

<br />

<table align="left">
<tr>
<td><strong>Backend</strong></td>
<td>Python 3, Django Framework</td>
</tr>
<tr>
<td><strong>Frontend</strong></td>
<td>JavaScript (ES6+), Bootstrap 5, HTML5/CSS3</td>
</tr>
<tr>
<td><strong>Database</strong></td>
<td>SQLite (Desenvolvimento)</td>
</tr>
<tr>
<td><strong>Lógica</strong></td>
<td>Fetch API (Requisições assíncronas), Django Paginator</td>
</tr>
</table>

<br clear="left"/>
<br />

---

<h2 align="left">🧠 Modelagem de Dados</h2>

<p align="left">
O desafio técnico central deste projeto foi a implementação de relacionamentos <strong>Many-to-Many</strong> no Django:
</p>

<ul>
  <li><strong>Post:</strong> Vinculado ao autor, contendo texto, timestamp e curtidas.</li>
  <li><strong>Follow:</strong> Uma tabela intermediária que conecta usuários a outros usuários (seguidores/seguindo).</li>
  <li><strong>Like:</strong> Relação entre usuários e postagens para garantir que um usuário só curta um post uma única vez.</li>
</ul>

###

<h2 align="left">📺 Demonstração em Vídeo</h2>

<div align="center">

https://github.com/user-attachments/assets/3b7d4622-4170-4a03-99fc-895eb0e018f0

  <br />
  <p>
    <a href="https://youtu.be/Z-McM0AQdw0" target="_blank">
      <strong>🚀 <i>Confira a demonstração no YouTube:</i></strong>
    </a>
