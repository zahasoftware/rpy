
set tardir=c:\temp\output\
set targetdir=c:\temp\output\lib\
set projectdir=C:\Proyectos\Raspberry\rpy\rnet\
set rpyprojectdir=C:\Proyectos\Raspberry\rpy\rpy\

set ftpuser=pi
set ftphostname=192.168.0.14

echo %tardir%
mkdir %targetdir%
cd %projectdir%
del /f %tardir%output.tar.gz
dotnet publish -r linux-arm -c debug -o %targetdir%

xcopy %rpyprojectdir%* %targetdir% /E /y
cd %targetdir%
tar -cvzf  %tardir%output.tar.gz ./*

cd %projectdir%Scripts\
c:\bin\psftp %ftpuser%@%ftphostname% -bc -b .\psftp.bat