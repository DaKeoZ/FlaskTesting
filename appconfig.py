import platform

where = platform.uname().release.find("aws")

if where == -1:
    config = {
        "host": "dakeoz.fr",
        "database": "testing",
        "user": "tester",
        "password": "testerpasswd",
    }
else:
    config = {
        "host": "C00277104.mysql.pythonanywhere-services.com",
        "database": "C00277104$default",
        "user": "C00277104",
        "password": "testerpasswd",
    }
