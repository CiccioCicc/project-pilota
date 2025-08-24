# Project Pilota – QA Infrastructure

Monorepo per:
- Test di performance (Locust) + metriche (Prometheus) + dashboard (Grafana)
- Test UI E2E (Playwright)
- CI (Jenkins)

## Struttura
- `perf/locust`: scenari e config Locust
- `perf/prometheus`: `prometheus.yml` e regole
- `perf/grafana`: dashboard JSON e provisioning
- `ui-tests`: Playwright e2e
- `infra`: docker-compose e container infra
- `ci`: Jenkinsfile e script

## Come iniziare (locale)
```bash
# Performance stack (esempio futuro)
docker compose -f infra/docker-compose.yml up -d
go
Copia
Modifica

## 2.4 `docs/STANDARD-GIT.md` (regole leggere)
`docs/STANDARD-GIT.md`:
```markdown
# Standard Git

## Branching
- `main`: branch stabile
- feature: `feat/<area>/<descrizione-corta>`
- fix: `fix/<area>/<bug-id>`

## Commit (Conventional Commits)
- `feat: ...`, `fix: ...`, `docs: ...`, `chore: ...`, `test: ...`, `refactor: ...`

## Pull Request
- PR piccole, con descrizione, link a issue/task
- Richiesta 1 review prima del merge su `main`
