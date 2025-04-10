# Changes

<!-- towncrier release notes start -->
## 1.0.0a5 (2025-04-09)

### Backend


#### Bug fixes:

- Passa o profile_id `portalbrasil.core:base` durante a criação de um novo site @ericof [#2](https://github.com/portal-br/core/issues/2)
- Imagem ghcr.io/portal-br/core-prod: Seta variável CHAMELEON_CACHE com valor de /data/cache @ericof [#3](https://github.com/portal-br/core/issues/3)



### Frontend

No significant changes.


### Projeto


#### Internal

- Atualiza versão da action docker/build-push-action de v5 para v6 @ericof 



## 1.0.0a4 (2025-04-09)

### Backend


#### New features:

- Gera imagens Docker base para uso das distribuições do PortalBrasil @ericof 



### Frontend

No significant changes.


### Projeto


#### Feature

- GHA: Altera workflows para a geração de imagens Docker base para uso das distribuições do PortalBrasil @ericof 



## 1.0.0a3 (2025-04-08)

### Backend


#### New features:

- Altera ordem dos campos no comportamento de configuração do rodapé @ericof 


#### Bug fixes:

- Refatora testes para que não quebrem após uma nova release @ericof 


#### Tests

- Disponibiliza portalbrasil.core.testing.layers.PortalBrasilDistributionFixture @ericof 



### Frontend

#### Feature

- Atualiza textos do rodapé @ericof 



### Projeto


#### Internal

- GHA: Adiciona workflow para changelog @ericof 



## 1.0.0a2 (2025-04-08)

### Backend


#### Internal:

- Corrige nome do arquivo de wheel publicado no PyPI. @ericof 



### Frontend

#### Bugfix

- Corrige problema com exibição de informações do projeto no componente VersionOverview @ericof 



### Projeto

Sem modificações.




## 1.0.0a1 (2025-04-08)

### Backend


#### New features:

- Adiciona Products.CMFPlone 6.1.1 como dependência @ericof 
- Adiciona plone.distribution 3.1.2 como dependência @ericof 
- Adiciona plonegovbr.brfields como dependência @ericof 
- Refatora @system para retornar informações sobre o PortalBrasil e a distribuição instalada @ericof 



### Frontend

#### Feature

- Adiciona @kitconcept/volto-light-theme 6.0 como dependência @ericof 
- Altera o componente VersionOverview do `@plone/volto` para exibir informações do PortalBrasil @ericof 



### Projeto


#### Feature

- Configuração inicial do repositório em github.co,/portal-br/core @ericof 


