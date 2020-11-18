#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neofetch
Version  : 7.1.0
Release  : 10
URL      : https://github.com/dylanaraps/neofetch/archive/7.1.0/neofetch-7.1.0.tar.gz
Source0  : https://github.com/dylanaraps/neofetch/archive/7.1.0/neofetch-7.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: neofetch-bin = %{version}-%{release}
Requires: neofetch-license = %{version}-%{release}
Requires: neofetch-man = %{version}-%{release}
Patch1: clearlinux.patch

%description
<h3 align="center"><img src="https://i.imgur.com/ZQI2EYz.png" alt="logo" height="100px"></h3>
<p align="center">A command-line system information tool written in bash 3.2+</p>

%package bin
Summary: bin components for the neofetch package.
Group: Binaries
Requires: neofetch-license = %{version}-%{release}

%description bin
bin components for the neofetch package.


%package license
Summary: license components for the neofetch package.
Group: Default

%description license
license components for the neofetch package.


%package man
Summary: man components for the neofetch package.
Group: Default

%description man
man components for the neofetch package.


%prep
%setup -q -n neofetch-7.1.0
cd %{_builddir}/neofetch-7.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605726232
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1605726232
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/neofetch
cp %{_builddir}/neofetch-7.1.0/LICENSE.md %{buildroot}/usr/share/package-licenses/neofetch/e79c0e7c09652ab87c5121d97f515d8b49ab3067
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neofetch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/neofetch/e79c0e7c09652ab87c5121d97f515d8b49ab3067

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/neofetch.1
