# PortalBrasil: Core 🚀

[![Built with Cookieplone](https://img.shields.io/badge/built%20with-Cookieplone-0083be.svg?logo=cookiecutter)](https://github.com/plone/cookieplone-templates/)
[![CI](https://github.com/portal-br/core/actions/workflows/main.yml/badge.svg)](https://github.com/portal-br/core/actions/workflows/main.yml)

Componentes base do PortalBrasil.

## Quick Start 🏁

### Prerequisites ✅

Ensure you have the following installed:

- UV 🐍
- Node 22 🟩
- pnpm 🧶
- Docker 🐳

### Installation 🔧

1. Clone the repository:

```shell
git clone git@github.com:portal-br/core.git
cd core
```

2. Install both Backend and Frontend:

```shell
make install
```

### Fire Up the Servers 🔥

1. Create a new Plone site on your first run:

```shell
make backend-create-site
```

2. Start the Backend at [http://localhost:8080/](http://localhost:8080/):

```shell
make backend-start
```

3. In a new terminal, start the Frontend at [http://localhost:3000/](http://localhost:3000/):

```shell
make frontend-start
```

Voila! Your Plone site should be live and kicking! 🎉

## Project Structure 🏗️

This monorepo consists of three distinct sections: `backend` and `frontend`.

- **backend**: Houses the API and Plone installation, utilizing pip instead of buildout, and includes a policy package named portalbrasil.core.
- **frontend**: Contains the React (Volto) package.


## Code Quality Assurance 🧐

It is possible to only run `format`:

```shell
make format
```

or `lint`:

 ```shell
make lint
```
Linters can be run individually within the `backend` or `frontend` folders.

## Internationalization 🌐

Generate translation files for Plone and Volto with ease:

```shell
make i18n
```

## Credits and Acknowledgements 🙏

Generated using [Cookieplone (0.8.4)](https://github.com/plone/cookieplone) and [cookieplone-templates (86480b4)](https://github.com/plone/cookieplone-templates/commit/86480b44baa3953c98534071089ac3c6b656f3f5) on 2025-03-23 14:53:53.605935. A special thanks to all contributors and supporters!
