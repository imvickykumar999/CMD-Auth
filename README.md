# `CMD Auth`

    There is no GUI for login or signup.

<br>

While `app.py` is running on one cmd, 

```bash
>>> python app.py

 * Serving Flask app 'app'
 * Debug mode: on

WARNING: This is a development server.
Do not use it in a production deployment.
Use a production WSGI server instead.

 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 142-206-457
```

run `python` in another cmd.

```bash
>>> import main

>>> main.crud_table()
>>> main.auth_table()

>>> main.get_req()
    Enter link : http://127.0.0.1:5000/logout

>>> main.post_req()
    Enter link : http://127.0.0.1:5000/login
```
