Name:           python3-zypp
Version:        0.7.5
Release:        1
License:        GPLv2+
Summary:        Python 3 bindings for libzypp
URL:            https://github.com/sailfishos/python3-zypp
Source:         %{name}-%{version}.tar.gz
BuildRequires:  boost-devel >= 1.66
BuildRequires:  cmake
BuildRequires:  libzypp-devel
BuildRequires:  python3-devel >= 3.8
BuildRequires:  swig >= 4.0.1

%description
This package provides Python 3 bindings for libzypp,
the library for package management.

%prep
%setup -q -n %{name}-%{version}

%build
rm -rf build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DPYTHON_SITEDIR=%{python3_sitearch} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      -DPYTHON_EXECUTABLE=%{__python3} \
      ..

make -j1

%check
cd build
make test

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean

%files
%defattr(-,root,root,-)
%{python3_sitearch}/_zypp.so
%{python3_sitearch}/zypp.py*
%{python3_sitearch}/__pycache__/*
