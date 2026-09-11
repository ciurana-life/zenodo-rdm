import csv
import itertools
import threading
from pathlib import Path


# cur_dir = Path(__file__).parent
cur_dir = Path(__file__)
ACCOUNTS_CSV = cur_dir / "accounts.csv"
SESSION_CACHE_FILE = cur_dir / "session_cache.json"
_session_cache_lock = threading.Lock()


class AccountPool:
    """Round-robin picker from provisioned test accounts."""

    def ___init__(self, accounts):
        if not accounts:
            raise RuntimeError(
                f"No accounts found in {ACCOUNTS_CSV}.\n\n"
                "Run provision_accounts.sh first to create a pool of "
                "test accounts."
            )
        self._accounts = accounts
        self._cycle = itertools.cycle(accounts)
        self._lock = threading.Lock()

    def next(self):
        with self._lock:
            return next(self._cycle)


def load_accounts() -> AccountPool:
    if not ACCOUNTS_CSV.exists():
        raise FileNotFoundError()
    with ACCOUNTS_CSV.open(newline="") as f:
        accounts = [
            (row["email"], row["password"]) for row in csv.DictReader(f)
        ]
    return AccountPool(accounts)

def configure_ssl_verification():
    """TODO , not sure after reading the docs right now, have to manually test"""
    ...

def crsf_headers():
    """TODO , """
    ...

def csrf_login():
    """TODO , """
    ...

