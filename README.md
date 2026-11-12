# Music_App

## Contributing

### Branch naming

Format: `type/short-description` — lowercase, words separated by hyphens.

| Type     | Use for                                          | Example                      |
| -------- | ------------------------------------------------ | ---------------------------- |
| `feat/`  | A new feature                                    | `feat/artist-resolution`     |
| `fix/`   | A bug fix                                        | `fix/musicbrainz-rate-limit` |
| `setup/` | Project setup and config                         | `setup/docker-compose`       |
| `test/`  | Adding or changing tests only                    | `test/playlist-rules`        |
| `docs/`  | README and documentation                         | `docs/contributing`          |
| `api/`   | OpenAPI schema changes (own PR, before the code) | `api/playlist-endpoint`      |

Rules:

- Never commit or push directly to `main`. All changes go through a pull request.
- One branch per task. Keep PRs small. Aim for one feature or fix each.
- Start every branch from an up-to-date `main`:
  ```bash
  git checkout main
  git pull
  git checkout -b feat/your-task
  ```

### Pull requests

- Every PR is reviewed by someone **outside** your workstream.
- Tests for a feature are written before the feature and must pass.
- "Done" means merged, deployed and tested.

### PR template

Copy this into your PR description:

```
## What
One or two sentences on what this PR does.

## Why
The task or problem it solves.

## How to test
Steps or commands to check it works, e.g. `pytest tests/test_artist_resolution.py`

## Checklist
- [ ] Branch is named `type/short-description`
- [ ] Tests written and passing
- [ ] No secrets or `.env` committed
- [ ] OpenAPI schema updated (if the API changed)
```
