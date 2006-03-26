Summary:	Nagios Nuvola Style
Summary(pl):	Styl Nuvola dla Nagiosa
Name:		nagios-theme-nuvola
Version:	1.0.3
Release:	2
License:	LGPL / Free (dtree)
Group:		Applications/WWW
Source0:	nagios-nuvola-%{version}.tar.gz
# Source0-md5:	3e8413932b1936192fdb4080ae90af20
Patch0:		nagios-nuvola-favicon.patch
URL:		http://tinyurl.com/a946b
BuildRequires:	sed >= 4.0
Requires:	nagios-cgi >= 2.0-0.b3.31
Provides:	nagios-theme
Obsoletes:	nagios-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_nagiosdir	/usr/share/nagios

%description
Complete Nagios Style (Menu, Icons, Stylesheets, Images) for Nagios
2.0.

Style had been updated to version 1.0 with the free DTree menu.

This is a complete image pack, menu and stylesheets for Nagios 2.0.
Icons are from the Nuvola KDE theme (http://www.icon-king.com/)

%description -l pl
Pe³ny styl Nagiosa (menu, ikony, arkusze styli, obrazki) dla Nagiosa
2.0.

Styl zosta³ uaktualniony do wersji 1.0 z darmowym menu DTree.

Jest to pe³ny pakiet obrazków, menu i arkuszy styli dla Nagiosa 2.0.
Ikony pochodz± z motywu KDE Nuvola (http://www.icon-king.com/).

%prep
%setup -q -c
# undos the sources
find . -type f '(' -name '*.html' -o -name '*.js' -o -name '*.css' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_nagiosdir}
cp -a html/* $RPM_BUILD_ROOT%{_nagiosdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
# well. should add it to /etc/nagios, but that means need  to enable FollowSymLinks directive in apache
%config(noreplace) %verify(not md5 mtime size) %{_nagiosdir}/config.js
%{_nagiosdir}/*.html
%{_nagiosdir}/images/*
%{_nagiosdir}/stylesheets/*
%{_nagiosdir}/side
