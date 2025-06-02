## 1.0.0a6 (2025-06-02)


### New features:

- Adiciona plonegovbr.socialmedia como dependência @ericof [#5](https://github.com/portal-br/core/issues/5)
- Adiciona `collective.volto.formsupport` como dependência. @ericof 


### Bug fixes:

- Corrige erro com a portal_migration quando acessada via ClassicUI. @ericof 


### Internal:

- Atualiza arquivos de tradução. @ericof 
- Atualiza plone.restapi para versão 9.14.0. @ericof 

## 1.0.0a5 (2025-04-09)


### Bug fixes:

- Passa o profile_id `portalbrasil.core:base` durante a criação de um novo site @ericof [#2](https://github.com/portal-br/core/issues/2)
- Imagem ghcr.io/portal-br/core-prod: Seta variável CHAMELEON_CACHE com valor de /data/cache @ericof [#3](https://github.com/portal-br/core/issues/3)

## 1.0.0a4 (2025-04-09)


### New features:

- Gera imagens Docker base para uso das distribuições do PortalBrasil @ericof 

## 1.0.0a3 (2025-04-08)


### New features:

- Altera ordem dos campos no comportamento de configuração do rodapé @ericof 


### Bug fixes:

- Refatora testes para que não quebrem após uma nova release @ericof 


### Tests

- Disponibiliza portalbrasil.core.testing.layers.PortalBrasilDistributionFixture @ericof 

## 1.0.0a2 (2025-04-08)


### Internal:

- Corrige nome do arquivo de wheel publicado no PyPI. @ericof 

## 1.0.0a1 (2025-04-08)


### New features:

- Adiciona Products.CMFPlone 6.1.1 como dependência @ericof 
- Adiciona plone.distribution 3.1.2 como dependência @ericof 
- Adiciona plonegovbr.brfields como dependência @ericof 
- Refatora @system para retornar informações sobre o PortalBrasil e a distribuição instalada @ericof
