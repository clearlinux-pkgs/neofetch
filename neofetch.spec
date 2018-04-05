#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neofetch
Version  : 3.4.0
Release  : 2
URL      : https://github.com/dylanaraps/neofetch/archive/3.4.0.tar.gz
Source0  : https://github.com/dylanaraps/neofetch/archive/3.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: neofetch-bin
Requires: neofetch-doc
Requires: neofetch-data

%description
# Neofetch
<a href="https://repology.org/metapackage/neofetch">
<img src="https://repology.org/badge/vertical-allrepos/neofetch.svg" alt="Packaging status" align="right" height="400px">
</a>

%package bin
Summary: bin components for the neofetch package.
Group: Binaries
Requires: neofetch-data

%description bin
bin components for the neofetch package.


%package data
Summary: data components for the neofetch package.
Group: Data

%description data
data components for the neofetch package.


%package doc
Summary: doc components for the neofetch package.
Group: Documentation

%description doc
doc components for the neofetch package.


%prep
%setup -q -n neofetch-3.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522969636
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1522969636
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neofetch

%files data
%defattr(-,root,root,-)
/usr/share/neofetch/ascii/distro/aix
/usr/share/neofetch/ascii/distro/alpine
/usr/share/neofetch/ascii/distro/alpine_small
/usr/share/neofetch/ascii/distro/amazon
/usr/share/neofetch/ascii/distro/anarchy
/usr/share/neofetch/ascii/distro/android
/usr/share/neofetch/ascii/distro/antergos
/usr/share/neofetch/ascii/distro/antix
/usr/share/neofetch/ascii/distro/aosc
/usr/share/neofetch/ascii/distro/apricity
/usr/share/neofetch/ascii/distro/arch
/usr/share/neofetch/ascii/distro/arch_old
/usr/share/neofetch/ascii/distro/arch_small
/usr/share/neofetch/ascii/distro/arch_xferience
/usr/share/neofetch/ascii/distro/archbox
/usr/share/neofetch/ascii/distro/archlabs
/usr/share/neofetch/ascii/distro/archmerge
/usr/share/neofetch/ascii/distro/artix
/usr/share/neofetch/ascii/distro/arya
/usr/share/neofetch/ascii/distro/bitrig
/usr/share/neofetch/ascii/distro/blag
/usr/share/neofetch/ascii/distro/blankon
/usr/share/neofetch/ascii/distro/bsd
/usr/share/neofetch/ascii/distro/bunsenlabs
/usr/share/neofetch/ascii/distro/calculate
/usr/share/neofetch/ascii/distro/centos
/usr/share/neofetch/ascii/distro/chakra
/usr/share/neofetch/ascii/distro/chaletos
/usr/share/neofetch/ascii/distro/chapeau
/usr/share/neofetch/ascii/distro/chrome
/usr/share/neofetch/ascii/distro/cloveros
/usr/share/neofetch/ascii/distro/coreos
/usr/share/neofetch/ascii/distro/crux
/usr/share/neofetch/ascii/distro/crux_small
/usr/share/neofetch/ascii/distro/debian
/usr/share/neofetch/ascii/distro/debian_small
/usr/share/neofetch/ascii/distro/deepin
/usr/share/neofetch/ascii/distro/desaos
/usr/share/neofetch/ascii/distro/devuan
/usr/share/neofetch/ascii/distro/dracos
/usr/share/neofetch/ascii/distro/dragonflybsd
/usr/share/neofetch/ascii/distro/dragonflybsd_old
/usr/share/neofetch/ascii/distro/dragonflybsd_small
/usr/share/neofetch/ascii/distro/elementary
/usr/share/neofetch/ascii/distro/endless
/usr/share/neofetch/ascii/distro/exherbo
/usr/share/neofetch/ascii/distro/fedora
/usr/share/neofetch/ascii/distro/freebsd
/usr/share/neofetch/ascii/distro/freebsd_small
/usr/share/neofetch/ascii/distro/frugalware
/usr/share/neofetch/ascii/distro/funtoo
/usr/share/neofetch/ascii/distro/galliumos
/usr/share/neofetch/ascii/distro/gem
/usr/share/neofetch/ascii/distro/gentoo
/usr/share/neofetch/ascii/distro/gentoo_small
/usr/share/neofetch/ascii/distro/gnewsense
/usr/share/neofetch/ascii/distro/gnu
/usr/share/neofetch/ascii/distro/gobolinux
/usr/share/neofetch/ascii/distro/grombyang
/usr/share/neofetch/ascii/distro/guixsd
/usr/share/neofetch/ascii/distro/haiku
/usr/share/neofetch/ascii/distro/hyperbola
/usr/share/neofetch/ascii/distro/irix
/usr/share/neofetch/ascii/distro/kali
/usr/share/neofetch/ascii/distro/kaos
/usr/share/neofetch/ascii/distro/kde
/usr/share/neofetch/ascii/distro/kogaion
/usr/share/neofetch/ascii/distro/korora
/usr/share/neofetch/ascii/distro/kslinux
/usr/share/neofetch/ascii/distro/kubuntu
/usr/share/neofetch/ascii/distro/lede
/usr/share/neofetch/ascii/distro/linux
/usr/share/neofetch/ascii/distro/lmde
/usr/share/neofetch/ascii/distro/lubuntu
/usr/share/neofetch/ascii/distro/lunar
/usr/share/neofetch/ascii/distro/mac
/usr/share/neofetch/ascii/distro/mac_small
/usr/share/neofetch/ascii/distro/mageia
/usr/share/neofetch/ascii/distro/magpieos
/usr/share/neofetch/ascii/distro/manjaro
/usr/share/neofetch/ascii/distro/maui
/usr/share/neofetch/ascii/distro/mer
/usr/share/neofetch/ascii/distro/minix
/usr/share/neofetch/ascii/distro/mint
/usr/share/neofetch/ascii/distro/mx
/usr/share/neofetch/ascii/distro/netbsd
/usr/share/neofetch/ascii/distro/netrunner
/usr/share/neofetch/ascii/distro/nitrux
/usr/share/neofetch/ascii/distro/nixos
/usr/share/neofetch/ascii/distro/nixos_small
/usr/share/neofetch/ascii/distro/nurunner
/usr/share/neofetch/ascii/distro/nutyx
/usr/share/neofetch/ascii/distro/obrevenge
/usr/share/neofetch/ascii/distro/openbsd
/usr/share/neofetch/ascii/distro/openbsd_small
/usr/share/neofetch/ascii/distro/openindiana
/usr/share/neofetch/ascii/distro/openmandriva
/usr/share/neofetch/ascii/distro/openwrt
/usr/share/neofetch/ascii/distro/oracle
/usr/share/neofetch/ascii/distro/osmc
/usr/share/neofetch/ascii/distro/pacbsd
/usr/share/neofetch/ascii/distro/parabola
/usr/share/neofetch/ascii/distro/pardus
/usr/share/neofetch/ascii/distro/parrot
/usr/share/neofetch/ascii/distro/parsix
/usr/share/neofetch/ascii/distro/pclinuxos
/usr/share/neofetch/ascii/distro/peppermint
/usr/share/neofetch/ascii/distro/pop_os
/usr/share/neofetch/ascii/distro/porteus
/usr/share/neofetch/ascii/distro/postmarketos
/usr/share/neofetch/ascii/distro/puppy
/usr/share/neofetch/ascii/distro/qubes
/usr/share/neofetch/ascii/distro/raspbian
/usr/share/neofetch/ascii/distro/redhat
/usr/share/neofetch/ascii/distro/redstar
/usr/share/neofetch/ascii/distro/refracta
/usr/share/neofetch/ascii/distro/rosa
/usr/share/neofetch/ascii/distro/sabayon
/usr/share/neofetch/ascii/distro/sabotage
/usr/share/neofetch/ascii/distro/sailfishos
/usr/share/neofetch/ascii/distro/salentos
/usr/share/neofetch/ascii/distro/scientific
/usr/share/neofetch/ascii/distro/siduction
/usr/share/neofetch/ascii/distro/slackware
/usr/share/neofetch/ascii/distro/slitaz
/usr/share/neofetch/ascii/distro/smartos
/usr/share/neofetch/ascii/distro/solaris
/usr/share/neofetch/ascii/distro/solus
/usr/share/neofetch/ascii/distro/source_mage
/usr/share/neofetch/ascii/distro/sparky
/usr/share/neofetch/ascii/distro/steamos
/usr/share/neofetch/ascii/distro/suse
/usr/share/neofetch/ascii/distro/swagarch
/usr/share/neofetch/ascii/distro/tails
/usr/share/neofetch/ascii/distro/trisquel
/usr/share/neofetch/ascii/distro/trueos
/usr/share/neofetch/ascii/distro/tumbleweed
/usr/share/neofetch/ascii/distro/ubuntu
/usr/share/neofetch/ascii/distro/ubuntu-budgie
/usr/share/neofetch/ascii/distro/ubuntu-gnome
/usr/share/neofetch/ascii/distro/ubuntu-mate
/usr/share/neofetch/ascii/distro/ubuntu-studio
/usr/share/neofetch/ascii/distro/ubuntu_old
/usr/share/neofetch/ascii/distro/void
/usr/share/neofetch/ascii/distro/void_small
/usr/share/neofetch/ascii/distro/windows
/usr/share/neofetch/ascii/distro/windows10
/usr/share/neofetch/ascii/distro/xubuntu
/usr/share/neofetch/ascii/distro/zorin

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
