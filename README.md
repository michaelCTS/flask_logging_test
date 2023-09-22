# Flask structured logging tests

Run with `python -m flask run`

## Setting the logging framework

Use the `LOG_FRAMEWORK` env-var to on of

- `json_logging`
- `loguru`
- `structlog`

## Debug mode

Enabling debug mode will turn off structured logging to improve developer experience.
It will thus log normally and you won't have to parse JSON while developing.

## Evaluation

Time of writing 2023-09-22.

|                             | json_logging | loguru       | structlog    |
|-----------------------------|--------------|--------------|--------------|
| uses stdlib `logging`       | yes          | no           | no           |
| last commit                 | [2022-11-5]  | [2023-09-11] | [2023-09-19] |
| maintained                  | ???          | yes          | yes          |
| Structured logging          | yes          | yes          | yes          |
| OOB Correlation-ID logging  | yes          | no           | no           |
| Correlation-ID generation   | yes          | no           | no           |
| Logger naming               | yes          | yes          | maybe?       |
| optional structured logging | yes          | yes          | yes          |

Optional requirements

|            | json_logging | loguru | structlog |
|------------|--------------|--------|-----------|
| log colors | no           | yes    | yes       |

[2022-11-5]: https://github.com/bobbui/json-logging-python/commit/403d8221795a6808f96be9d24a9d97250fcd293e

[2023-09-11]: https://github.com/Delgan/loguru/commit/e1f48c91cf2646b6429020f784881cd200663114

[2023-09-19]: https://github.com/hynek/structlog/commit/bb1799fec665025f2a1e4eec4d71218d72bfe959

## `json_logging`

Is the easiest to use with Flask.
The only downside is that it's not clear whether it's still maintained.

**Example log output**

```json
{
  "written_at": "2023-09-22T08:13:52.968Z",
  "written_ts": 1695370432968949000,
  "type": "request",
  "correlation_id": "f7b3e876-591f-11ee-832c-98597af1829f",
  "remote_user": "-",
  "request": "/",
  "referer": "-",
  "x_forwarded_for": "-",
  "protocol": "HTTP/1.1",
  "method": "GET",
  "remote_ip": "127.0.0.1",
  "request_size_b": -1,
  "remote_host": "127.0.0.1",
  "remote_port": 39438,
  "request_received_at": "2023-09-22T08:13:52.968Z",
  "response_time_ms": 0,
  "response_status": 200,
  "response_size_b": 12,
  "response_content_type": "text/html; charset=utf-8",
  "response_sent_at": "2023-09-22T08:13:52.968Z"
}
```

## `loguru`

A good logger that works out of the box on new projects without any setup.
Its selling point is that you use a singler `logger` everywhere.
Import it and call `log.info` or whatever and you're done.

However, it is its own logging framework and doesn't use the logging from stdlib.
That means custom [code has to be written](https://github.com/Delgan/loguru#entirely-compatible-with-standard-logging)
to handle libraries that do log using the stdlib.

Log level configuration involves adding a logger with a filter at the desired level.
One then has to remember to remove other loggers, otherwise there are multiple loggers.
It isn't as simple as stdlib `logger.setLevel()` and you're done.

**Example log output**

```json
{
  "text": "2023-09-22 10:12:58.082 | INFO     | endpoints.hello:say_hello:8 - about to say hello\n",
  "record": {
    "elapsed": {
      "repr": "0:00:12.520662",
      "seconds": 12.520662
    },
    "exception": null,
    "extra": {},
    "file": {
      "name": "hello.py",
      "path": "/home/michael/projects/other/flaskProject/endpoints/hello.py"
    },
    "function": "say_hello",
    "level": {
      "icon": "ℹ️",
      "name": "INFO",
      "no": 20
    },
    "line": 8,
    "message": "about to say hello",
    "module": "hello",
    "name": "endpoints.hello",
    "process": {
      "id": 234206,
      "name": "MainProcess"
    },
    "thread": {
      "id": 139874679666368,
      "name": "Thread-1 (process_request_thread)"
    },
    "time": {
      "repr": "2023-09-22 10:12:58.082316+02:00",
      "timestamp": 1695370378.082316
    }
  }
}
```

## `structlog`

Another self-rolled logging framework, which comes with the same caveats as `loguru`.
It doesn't use the "one to rule them all" approach though.

It takes more fiddling with the formatter for stdlib than with `loguru` and I haven't figured it out yet.
The logs are minimal.

**Example log output**

```json

```