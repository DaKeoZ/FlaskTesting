import platform

where = platform.uname().release.find("aws")

if where == -1:
    # Local.
    config = {
        "host": "dakeoz.fr",
        "database": "testing",
        "user": "tester",
        "password": "testerpasswd",
    }
else:
    # Not on PA.
    """config = {
        "host": "c3macs.mysql.pythonanywhere-services.com",
        "database": "c3macs$default",
        "user": "c3macs",
        "password": "passwordhere",
    }"""
    config = {
        "host": "dakeoz.fr",
        "database": "testing",
        "user": "tester",
        "password": "testerpasswd",
    }
