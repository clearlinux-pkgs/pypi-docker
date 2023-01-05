#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docker
Version  : 6.0.1
Release  : 90
URL      : https://files.pythonhosted.org/packages/79/26/6609b51ecb418e12d1534d00b888ce7e108f38b47dc6cd589598d5c6aaa2/docker-6.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/79/26/6609b51ecb418e12d1534d00b888ce7e108f38b47dc6cd589598d5c6aaa2/docker-6.0.1.tar.gz
Summary  : A Python library for the Docker Engine API.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-docker-license = %{version}-%{release}
Requires: pypi-docker-python = %{version}-%{release}
Requires: pypi-docker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pywin32)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(websocket_client)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Docker SDK for Python
[![Build Status](https://github.com/docker/docker-py/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/docker/docker-py/actions/workflows/ci.yml/)

%package license
Summary: license components for the pypi-docker package.
Group: Default

%description license
license components for the pypi-docker package.


%package python
Summary: python components for the pypi-docker package.
Group: Default
Requires: pypi-docker-python3 = %{version}-%{release}

%description python
python components for the pypi-docker package.


%package python3
Summary: python3 components for the pypi-docker package.
Group: Default
Requires: python3-core
Provides: pypi(docker)
Requires: pypi(packaging)
Requires: pypi(paramiko)
Requires: pypi(pywin32)
Requires: pypi(requests)
Requires: pypi(urllib3)
Requires: pypi(websocket_client)

%description python3
python3 components for the pypi-docker package.


%prep
%setup -q -n docker-6.0.1
cd %{_builddir}/docker-6.0.1
pushd ..
cp -a docker-6.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672269097
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docker
cp %{_builddir}/docker-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-docker/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-docker/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
