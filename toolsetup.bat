@REM
@REM Copyright (c) 2007, Intel Corporation
@REM All rights reserved. This program and the accompanying materials
@REM are licensed and made available under the terms and conditions of the BSD License
@REM which accompanies this distribution.  The full text of the license may be found at
@REM http://opensource.org/licenses/bsd-license.php
@REM
@REM THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
@REM WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
@REM

@echo off

REM ##############################################################
REM # You should not have to modify anything below this line
REM #

REM
REM check the EDK_TOOLS_PATH
REM
:check_vc
if defined VCINSTALLDIR goto check_path
if defined VS71COMNTOOLS (
  call "%VS71COMNTOOLS%\vsvars32.bat"
) else (
  echo.
  echo !!! WARNING !!!! Cannot find Visual Studio !!!
  echo.
)

:check_path
if not defined PYTHON_FREEZER_PATH set PYTHON_FREEZER_PATH=C:\cx_Freeze

pushd .
cd %~dp0
set BASE_TOOLS_PATH=%CD%
popd

if not defined EDK_TOOLS_PATH set EDK_TOOLS_PATH=%BASE_TOOLS_PATH%
mkdir %EDK_TOOLS_PATH%\Bin\Win32

if not defined ORIGINAL_PATH set ORIGINAL_PATH=%PATH%
set PATH=%EDK_TOOLS_PATH%\Bin\Win32;%EDK_TOOLS_PATH%\Bin;%ORIGINAL_PATH%

:path_ok

if /I "%1"=="-h" goto Usage
if /I "%1"=="-help" goto Usage
if /I "%1"=="--help" goto Usage
if /I "%1"=="/h" goto Usage
if /I "%1"=="/?" goto Usage
if /I "%1"=="/help" goto Usage
if /I "%1"=="build" goto build
if /I "%1"=="rebuild" goto rebuild
if NOT "%1"=="" goto Usage

IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\BootSectImage.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\build.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\EfiLdrImage.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\EfiRom.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenBootSector.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenFds.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenFfs.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenFv.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenFw.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenPage.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenSec.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\GenVtf.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\MigrationMsa2Inf.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\Split.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\TargetTool.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\TianoCompress.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\Trim.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\VfrCompile.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\Fpd2Dsc.exe" goto build
IF NOT EXIST "%EDK_TOOLS_PATH%\Bin\Win32\VolInfo.exe" goto build

:skipbuild
goto end

:rebuild
pushd .
cd %BASE_TOOLS_PATH%
call nmake cleanall
del /f /q %BASE_TOOLS_PATH%\Bin\Win32\*.*
popd

:build
REM
REM Start to build the Framework Tools
REM

pushd .
cd %BASE_TOOLS_PATH%
call nmake
popd

goto end

:no_tools_path
echo.
echo !!!WARNING!!! No tools path found. Please check and set EDK_TOOLS_PATH.
echo.
goto end

:Usage
echo.
echo  Usage: %0 [build] [rebuild]
echo         build:    Incremental build, only build those updated tools; 
echo         rebuild:  Rebuild all tools neither updated or not; 
echo.

:end
@echo on

