%define		dictname vietanh
Summary:	Vietnamese-English dictionary for dictd
Summary(pl):	S³ownik wietnamsko-angielski dla dictd
Name:		dict-%{dictname}
Version:	1.0
Release:	1
License:	GPL (?)
Group:		Applications/Dictionaries
Source0:	http://vietlug.sourceforge.net/download/emacs/%{dictname}.index
Source1:	http://vietlug.sourceforge.net/download/emacs/%{dictname}.telex.dz
URL:		http://vietlug.sourceforge.net/
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vietnamese-English dictionary for dictd.

%description -l pl
S³ownik wietnamsko-angielski dla dictd.

%prep
%setup -C

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/dictd
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/dictd/%{dictname}.dict.dz

dictprefix=%{_datadir}/dictd/%{dictname}
echo "# Vietnamese-English dictionary
database %{dictname} {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}.dictconf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
