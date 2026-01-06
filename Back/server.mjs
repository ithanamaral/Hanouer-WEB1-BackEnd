import { createServer } from 'node:http';

const server = createServer((request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain; charset=utf-8');
    response.end('Alo galerinha de cowboy!');
});

server.listen(3000, () => {
    console.log('Tudo certo aqui patrão! Rodando na port 3000');
});