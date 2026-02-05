@echo off
setlocal

set PORT=55555
set ADDR=127.0.0.1

python output.py
python -m http.server %PORT% --bind %ADDR%
