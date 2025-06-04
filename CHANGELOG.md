# Changes

<!-- towncrier release notes start -->
## 1.0.0a8 (2025-06-04)

### Backend


#### New features:

- Adiciona o comportamento de título de navegação a todos os tipos de conteúdo. @ericof [#7](https://github.com/portal-br/core/issues/7)
- Atualiza plonegovbr.socialmedia para versão 2.0.0a6 @ericof [#12](https://github.com/portal-br/core/issues/12)
- Adiciona suporte ao versionamento de tipos de conteúdos. @ericof 


#### Internal:

- Registra distribuições que dependem deste pacote para serem atualizadas. @ericof 



### Frontend

#### Feature

- Visualizador de PDF na visão padrão de arquivo. @ericof [#9](https://github.com/portal-br/core/issue/9)
- Atualiza @kitconcept/volto-light-theme para versão 7.0.0-alpha.7 @ericof [#10](https://github.com/portal-br/core/issue/10)
- Atualiza @plone-collective/volto-authomatic para versão 3.0.0-alpha.3 @ericof [#11](https://github.com/portal-br/core/issue/11)
- Atualiza @plonegovbr/volto-social-media para versão 2.0.0-alpha.6 @ericof [#12](https://github.com/portal-br/core/issue/12)

#### Bugfix

- Corrige exibição do menu expandido. @ericof [#8](https://github.com/portal-br/core/issue/8)



### Projeto

Sem modificações.




## 1.0.0a7 (2025-06-02)

### Backend

Sem modificações.




### Frontend

#### Bugfix

- Corrige mapeamento de propriedades utilizadas pelos logos do rodapé. @ericof 



### Projeto

Sem modificações.




## 1.0.0a6 (2025-06-02)

### Backend


#### New features:

- Adiciona plonegovbr.socialmedia como dependência @ericof [#5](https://github.com/portal-br/core/issues/5)
- Adiciona `collective.volto.formsupport` como dependência. @ericof 


#### Bug fixes:

- Corrige erro com a portal_migration quando acessada via ClassicUI. @ericof 


#### Internal:

- Atualiza arquivos de tradução. @ericof 
- Atualiza plone.restapi para versão 9.14.0. @ericof 



### Frontend

#### Feature

- Adiciona dependência @plonegovbr/volto-social-media e remove @plonegovbr/volto-network-block @ericof [#5](https://github.com/portal-br/core/issue/5)
- Adiciona `@plone-collective/volto-authomatic` como dependência. @ericof 
- Atualiza @plone/volto para versão 18.22.0. @ericof 
- Atualiza `@kitconcept/volto-light-theme` para versão 6.2.0. @ericof 
- Atualiza `@kitconcept/volto-social-blocks` para versão 1.0.0-alpha.8. @ericof 
- Atualiza `@plonegovbr/volto-social-media` para versão 2.0.0-alpha.5. @ericof 

#### Bugfix

- Corrige o componente `UpgradeControlPanel`. @ericof 

#### Internal

- Atualiza arquivos de tradução. @ericof 



### Projeto


#### Internal

- Utiliza workflows compartilhados em plone/meta. @ericof 



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


