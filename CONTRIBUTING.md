# Guia de Contribuição para Iniciantes

Este tutorial vai te guiar por todas as etapas para contribuir com o repositório de forma profissional, mesmo que você nunca tenha usado GitHub antes. Siga o passo a passo e abra uma Pull Request (PR) padronizada!

---
## 1. Faça um Fork do Repositório

1. Acesse o repositório principal: [Jcnok/fastapi-docker-bootcamp](https://github.com/Jcnok/fastapi-docker-bootcamp)
2. Clique em "Fork" (canto superior direito).
3. Seu fork será criado no seu perfil do GitHub.

## 2. Clone o Fork Para Sua Máquina Local

Abra o terminal e execute:

```bash
git clone https://github.com/SEU_USUARIO/fastapi-docker-bootcamp.git
```
Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub.

## 3. Crie uma Branch Para a Sua Contribuição

```bash
cd fastapi-docker-bootcamp
git checkout -b minha-contribuicao
```
Escolha um nome representativo para a branch!

## 4. Execute o Projeto Localmente

**Com Docker:**

```bash
docker build -t fastapi-bootcamp .
docker run -d -p 8000:8000 fastapi-bootcamp
```

**Sem Docker (puro Python):**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

## 5. Realize Suas Alterações

- Edite arquivos, crie ou corrija funcionalidades conforme documentação
- Siga sempre as boas práticas apoiadas no repositório

## 6. Suba Suas Alterações Para o GitHub

```bash
git add .
git commit -m "Descreva sua contribuição"
git push origin minha-contribuicao
```

## 7. Abra uma Pull Request (PR)

- No seu fork, clique em "Compare & Pull Request"
- Preencha o template disponível ([veja exemplo](https://github.com/Jcnok/fastapi-docker-bootcamp/blob/main/.github/pull_request_template.md))
- Explique claramente sua contribuição
- Marque a issue relacionada, se houver

## 8. Padrões de PR e Checklist

- Preencha todos os itens do checklist [do template de PR](https://github.com/Jcnok/fastapi-docker-bootcamp/blob/main/.github/pull_request_template.md)
- Garanta que a build local está funcionando
- Adicione testes se possível

## 9. Como Abrir Uma Issue

- Use o template disponível ([veja exemplo](https://github.com/Jcnok/fastapi-docker-bootcamp/blob/main/.github/issue_template.md))
- Descreva detalhadamente sua sugestão, bug ou melhoria
- Adicione prints, exemplos ou contexto relevante

## 10. Comunique-se!

- Use as issues para dúvidas, sugestões ou combinar trabalho
- Seja cordial, detalhista e colaborativo

---
**Referências Úteis:**
- [Documentação GitHub](https://docs.github.com/pt)
- [FastAPI Docs](https://fastapi.tiangolo.com/pt/)
- [Docker Docs](https://docs.docker.com/pt/)

---
## Dúvidas? Crie uma issue ou pergunte no grupo!

Bom hacking 🚀
