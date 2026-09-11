# Locust load tests


## 1. Install

```bash
# Install + cache on tmp env
uv run --with locust locust --version

# Run commands
uv run --with locust <command>

# Or install on env
uv pip install locust
```

## 2. Initial configuration

### 2.1 Users
There is a wrapper for `invenio users create` that loops `n` times and provides active and confirmed users, they get saved in `accounts.csv` (gitignored)

Example:
```bash
# Local dev environment
./provision_accounts.sh 20
```

**TODO** Run on dev.zenodo.org , share with other team members

After login (first run) this accounts will add data to `session_cache.json` so that they don't need to login on every run. This is done because login-in users is very slow (by design by any hashing algorithm).

If you have some users created alrready you can manually fill the `accounts.csv` file with the format:
```csv
TODO: format and example
```

### 2.2 https (note TODO local)

FastHttpUser with insecure=True? I mean there is a locust file here that is old and uses normal HttpUser.

### 2.3 ENV (local)
Rate limit env to enale disable locally?
INVENIO_RATELIMIT_ENABLED ? 

## 3. Run

> **⚠️ Exception** <br>
> Don't try and run `iiif.py` with `--host={SOMETHING}` Since it takes it from `manifest.json` file.

Run scenario blueprint:
```bash
uv run --with locust locust -f <file_path.py> \
--host <https://127.0.0.1:5000 | https://dev.zenodo.org> \
--headless -u 10 -r 2 -t 5m
# -u --> num of users
# -r --> num of users to spawn per second
# -t --> time to run the scenario
```

> **`"-r"` is important to have in mind, if we don't have a `session_cache.json` file with some data, it is better to have a low spawn rate of users or we will create a login storm.**

Example read load:
```
uv run --with locust locust -f reads.py \
--host=https://127.0.0.1:5000 \
--headless -u 20 -r 2 -t 5m
```
