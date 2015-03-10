#### useful python scripts

---

#### mylogger.py
python logging module config, support log file path and backup logfile
usage:
```python
from mylogger import get_logger

# the simplest way
applog = get_logger('app')

# complex way
applog = get_logger('app', 'customer_log_path', one_file_size, backup_count)
```
