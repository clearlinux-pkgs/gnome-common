#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : gnome-common
Version  : 3.18.0
Release  : 12
URL      : https://download.gnome.org/sources/gnome-common/3.18/gnome-common-3.18.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-common/3.18/gnome-common-3.18.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-common-bin = %{version}-%{release}
Requires: gnome-common-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This module contains various files needed to bootstrap GNOME modules
built from git.  It contains the following components:
1. A common "autogen.sh" script that can be used to configure a
source directory checked out from git.
2. Some commonly used macros (quite a small set these days -- macros
should be packaged with their respective modules).

%package bin
Summary: bin components for the gnome-common package.
Group: Binaries
Requires: gnome-common-license = %{version}-%{release}

%description bin
bin components for the gnome-common package.


%package dev
Summary: dev components for the gnome-common package.
Group: Development
Requires: gnome-common-bin = %{version}-%{release}
Provides: gnome-common-devel = %{version}-%{release}
Requires: gnome-common = %{version}-%{release}

%description dev
dev components for the gnome-common package.


%package license
Summary: license components for the gnome-common package.
Group: Default

%description license
license components for the gnome-common package.


%prep
%setup -q -n gnome-common-3.18.0
cd %{_builddir}/gnome-common-3.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680027587
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1680027587
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-common
cp %{_builddir}/gnome-common-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-common/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/share/aclocal/ax_code_coverage.m4
rm -f %{buildroot}*/usr/share/aclocal/ax_check_enable_debug.m4

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-autogen.sh

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-common/4cc77b90af91e615a64ae04893fdffa7939db84c
