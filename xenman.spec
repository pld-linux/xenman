Summary:	A graphical Xen management tool
Summary(pl.UTF-8):	Graficzne narzędzie do zarządzania środowiskiem Xen
Name:		xenman
Version:	0.4.2.1
Release:	0.1
License:	LGPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/xenman/%{name}-%{version}.tar.gz
# Source0-md5:	dbafead7dbf5f98ff603113110fdfa17
URL:		http://xenman.sourceforge.net/
Requires:	xen >= 3.0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XenMan is a Xen management tool with a GTK+ based graphical interface
that allows for performing the standard set of domain operations
(start, stop, pause, kill, shutdown, reboot, snapshot, etc...). It
also attempts to simplify certain aspects such as the creation of
domains, as well as making the consoles available directly within the
tool's user interface.

%description -l pl.UTF-8
XenMan to narzędzie do zarządzania środowiskiem Xen z opartym na GTK+
graficznym interfejsem pozwalającym na wykonywanie standardowego
zestawu operacji na domenach (uruchamianie, zatrzymywanie, pauzowanie,
zabijanie, wyłączanie, rebootowanie, snapshot itp.). Próbuje także
uprościć pewne aspekty, takie jak tworzenie domen, a także
udostępnianie konsoli bezpośrednio w interfejsie użytkownika.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/pixmaps,%{_sbindir},%{_localstatedir}/cache/%{name}}

#install -Dp %{name}.conf-%{distext} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

install -Dp %{name}.py $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.py
install -Dp %{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.glade
install -Dp pixmaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps

ln -s ../share/%{name}/%{name}.py $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog.txt
#%config %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_sbindir}/%{name}
%{_datadir}/%{name}
%dir %{_localstatedir}/cache/%{name}
