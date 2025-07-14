Summary:	etherwake - send a wake-on-lan packet
Summary(pl.UTF-8):	etherwake - wysyła pakiet WOL
Name:		etherwake
Version:	1.09
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/e/etherwake/%{name}_%{version}.orig.tar.gz
# Source0-md5:	628e8b2a28d47f262e4c26c989402a59
Patch0:		http://ftp.debian.org/debian/pool/main/e/etherwake/%{name}_%{version}-3.diff.gz
# Patch0-md5:	c6fbb2cfde669866d67f6cf8c2cc686b
Patch1:		%{name}-build.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WakeLan sends a properly formatted UDP packet across the network which
will cause a wake-on-lan enabled computer to power on.

%description -l pl.UTF-8
WakeLan wysyła pakiet UDP przez sieć, który powoduje włączenie
komputera z WOL.

%prep
%setup -q -n %{name}-%{version}.orig
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install etherwake.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/etherwake
%{_mandir}/man8/etherwake.8*
