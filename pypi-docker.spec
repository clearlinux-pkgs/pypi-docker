#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docker
Version  : 5.0.3
Release  : 81
URL      : https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
Summary  : A Python library for the Docker Engine API.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-docker-license = %{version}-%{release}
Requires: pypi-docker-python = %{version}-%{release}
Requires: pypi-docker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(appdirs)
BuildRequires : pypi(asn1crypto)
BuildRequires : pypi(backports.ssl_match_hostname)
BuildRequires : pypi(cffi)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(enum34)
BuildRequires : pypi(idna)
BuildRequires : pypi(ipaddress)
BuildRequires : pypi(packaging)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(pywin32)
BuildRequires : pypi(requests)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(websocket_client)

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
Requires: pypi(requests)
Requires: pypi(websocket_client)

%description python3
python3 components for the pypi-docker package.


%prep
%setup -q -n docker-5.0.3
cd %{_builddir}/docker-5.0.3
pushd ..
cp -a docker-5.0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656407279
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docker
cp %{_builddir}/docker-5.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-docker/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
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
