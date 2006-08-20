Summary:	A graphical Xen management tool
Summary(pl):	Graficzne narzêdzie do zarz±dzania ¶rodowiskiem Xen
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

%description -l pl
XenMan to narzêdzie do zarz±dzania ¶rodowiskiem Xen z opartym na GTK+
graficznym interfejsem pozwalaj±cym na wykonywanie standardowego
zestawu operacji na domenach (uruchamianie, zatrzymywanie, pauzowanie,
zabijanie, wy³±czanie, rebootowanie, snapshot itp.). Próbuje tak¿e
upro¶ciæ pewne aspekty, takie jak tworzenie domen, a tak¿e
udostêpnianie konsoli bezpo¶rednio w interfejsie u¿ytkownika.

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
