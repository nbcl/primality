py_ver = sys.version_info
if py_ver.minor < 8 or py_ver.major < 3:
    msg = """
    Primality requires Python >= 3.8 to run
    Once you have Python 3.8 or greater installed you can use Primality:
    1. Create and activate venv:
        python3 -m venv venv
        source venv/bin/activate
    2. Install Primality:
        pip3 install primality
    More instructions at https://github.com/nbcl/primality/blob/main/docs"""
    print(msg)
    exit()
