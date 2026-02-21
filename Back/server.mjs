import { createServer } from 'node:http';

const server = createServer((request, response) => {
  // 1. Configuramos o cabeçalho para dizer que vamos enviar JSON (padrão de APIs)
  response.setHeader('Content-Type', 'application/json');
  request.method === 'GET';
  request.url === '/produtos';

  // Rota de Home
  if (request.method === 'GET' && request.url === '/') {
    response.statusCode = 200;
    response.end(JSON.stringify({ message: "Bem-vindo à Home da API!" }));
  } 
 
  // 2. Rota de Produtos (Simulando uma busca no banco)
  else if (request.method === 'GET' && request.url === '/produtos') {
    const listaProdutos = [
      { id: 1, nome: "Notebook Ryzen 5", preco: 3500 },
      { id: 2, nome: "Mouse Gamer", preco: 150 },
      { id: 3, nome: "Monitor 144hz", preco: 1200 }
    ];

    response.statusCode = 200;
    // Transformamos o array de objetos em uma String JSON
    console.log(JSON.stringify(listaProdutos));
    response.end(JSON.stringify(listaProdutos));
  } 

  // Rota não encontrada
  else {
    response.statusCode = 404;
    response.end(JSON.stringify({ error: "Rota não encontrada." }));
  }
});

server.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
});