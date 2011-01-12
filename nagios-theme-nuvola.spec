Summary:	Nagios Nuvola Style
Summary(pl.UTF-8):	Styl Nuvola dla Nagiosa
Name:		nagios-theme-nuvola
Version:	1.0.3
Release:	7
License:	LGPL / Free (dtree)
Group:		Applications/WWW
Source0:	nagios-nuvola-%{version}.tar.gz
# Source0-md5:	3e8413932b1936192fdb4080ae90af20
Source1:	sblogo.gif
# Source1-md5:	e4f6fec2b77f2db2103a966d824e2844
Patch0:		nagios-nuvola-favicon.patch
Patch1:		nagios-nuvola-texts.patch
Patch2:		%{name}-logo.patch
Patch3:		menu.patch
Patch4:		nagios-core.patch
URL:		http://exchange.nagios.org/directory/Addons/Frontends-%28GUIs-and-CLIs%29/Web-Interfaces/Themes-and-Skins/Nuvola-Style/details
BuildRequires:	sed >= 4.0
Requires:	nagios-cgi >= 2.0-0.b3.31
Provides:	nagios-theme
Obsoletes:	nagios-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_nagiosdir	/usr/share/nagios

%description
Complete Nagios Style (Menu, Icons, Stylesheets, Images) for Nagios.

Style had been updated to version 1.0 with the free DTree menu.

This is a complete image pack, menu and stylesheets for Nagios. Icons
are from the Nuvola KDE theme <http://www.icon-king.com/>.

Animated Nagios logo from NagioSexchange project #2343.

%description -l pl.UTF-8
Pełny styl Nagiosa (menu, ikony, arkusze styli, obrazki) dla Nagiosa.

Styl został uaktualniony do wersji 1.0 z darmowym menu DTree.

Jest to pełny pakiet obrazków, menu i arkuszy styli dla Nagiosa. Ikony
pochodzą z motywu KDE Nuvola <http://www.icon-king.com/>.

%prep
%setup -qc
# undos the sources
find . -type f '(' -name '*.html' -o -name '*.js' -o -name '*.css' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_nagiosdir}
cp -a html/* $RPM_BUILD_ROOT%{_nagiosdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_nagiosdir}/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
# well. should add it to /etc/nagios, but that means need to enable FollowSymLinks directive in apache
%config(noreplace) %verify(not md5 mtime size) %{_nagiosdir}/config.js
%{_nagiosdir}/*.html
%{_nagiosdir}/images/*
%{_nagiosdir}/stylesheets/*
%{_nagiosdir}/side
