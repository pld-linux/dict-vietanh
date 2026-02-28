%define		dictname vietanh
Summary:	Vietnamese-English dictionary for dictd
Summary(pl.UTF-8):	Słownik wietnamsko-angielski dla dictd
Name:		dict-%{dictname}
Version:	1.0
Release:	5
License:	GPL (?)
Group:		Applications/Dictionaries
Source0:	http://vietlug.sourceforge.net/download/emacs/%{dictname}.index
# Source0-md5:	bf0436710baba2be46e6d8177409cac7
Source1:	http://vietlug.sourceforge.net/download/emacs/%{dictname}.telex.dz
# Source1-md5:	4a4a9f37916d3db0d4ca3ab0e7381927
URL:		http://vietlug.sourceforge.net/
Requires:	%{_sysconfdir}/dictd
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vietnamese-English dictionary for dictd.

%description -l pl.UTF-8
Słownik wietnamsko-angielski dla dictd.

%prep

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
%service -q dictd restart

%postun
if [ "$1" = 0 ]; then
	%service -q dictd restart
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
