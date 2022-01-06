#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docker
Version  : 5.0.3
Release  : 76
URL      : https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
Summary  : A Python library for the Docker Engine API.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-docker-license = %{version}-%{release}
Requires: pypi-docker-python = %{version}-%{release}
Requires: pypi-docker-python3 = %{version}-%{release}
Requires: docker-pycreds
BuildRequires : buildreq-distutils3
Provides: docker-py
Provides: docker-py-python
Provides: docker-py-python3
BuildRequires : docker-pycreds
BuildRequires : pip
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
BuildRequires : setuptools-python
BuildRequires : websocket_client

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
Requires: pypi(appdirs)
Requires: pypi(asn1crypto)
Requires: pypi(backports.ssl_match_hostname)
Requires: pypi(cffi)
Requires: pypi(cryptography)
Requires: pypi(enum34)
Requires: pypi(idna)
Requires: pypi(ipaddress)
Requires: pypi(packaging)
Requires: pypi(paramiko)
Requires: pypi(pycparser)
Requires: pypi(pyopenssl)
Requires: pypi(pyparsing)
Requires: pypi(pywin32)
Requires: pypi(requests)
Requires: pypi(urllib3)
Requires: pypi(websocket_client)

%description python3
python3 components for the pypi-docker package.


%prep
%setup -q -n docker-5.0.3
cd %{_builddir}/docker-5.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641433864
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docker
cp %{_builddir}/docker-5.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-docker/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
