# About

This is my personal website. You can visit at [https://henriaidasso.me/](https://henriaidasso.me/)

Build using [tailpages](https://github.com/ahenrij/tailpages) started from this Harry Wang's [code base](https://github.com/harrywang/tailpages)

## Getting Started

### Prerequisites

- [Ruby](https://www.ruby-lang.org/) with [Bundler](https://bundler.io/)
- [Node.js](https://nodejs.org/) with npm
- [Docker](https://www.docker.com/) (optional, for the Docker-based setup)

### Option 1. Docker (recommended)

```bash
./scripts/start.sh
```

This starts Jekyll (with live reload) via Docker Compose and watches Tailwind CSS for changes. The site is available at `http://localhost:4000`.

### Option 2. Local setup

1. Install Ruby dependencies:
   ```bash
   bundle install
   ```

2. Install Node dependencies:
   ```bash
   npm install
   ```

3. In one terminal, watch Tailwind CSS:
   ```bash
   npx tailwindcss -i ./assets/css/main.css -o ./assets/css/tailwind.css --watch
   ```

4. In another terminal, serve the site:
   ```bash
   bundle exec jekyll serve
   ```

The site will be available at `http://localhost:4000`.
