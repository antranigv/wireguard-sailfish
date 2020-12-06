#
# spec file for WireGuard on Sailfish
#
Summary: WireGuard for Sailfish
Name: wireguard-sailfish
Version: 0.1
Release: 1
License: GPL
Vendor: WireGuard
Packager: Antranig Vartanian <antranig@vartanian.am>
Source0: https://antranigv.am/misc/wireguard-sailfish.tar.gz

%description
WireGuard: fast, modern, secure VPN tunnel. This is the Sailfish version.

%prep

%build

%install
cd %{name}
make install

%files
/usr/bin/wg
/usr/bin/wg-quick
/usr/bin/wireguard-go

