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
tar xf ${RPM_SOURCE_DIR}/wireguard-sailfish.tar.gz

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 wg wg-quick wireguard-go %{buildroot}/%{_bindir}/

%files
/usr/bin/wg
/usr/bin/wg-quick
/usr/bin/wireguard-go

