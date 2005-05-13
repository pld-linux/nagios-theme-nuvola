Summary:	Nagios Nuvola Style
Name:		nagios-theme-nuvola
Version:	1.0
Release:	0.2
License:	Open Source
Group:		Applications/WWW
# Saved from http://tinyurl.com/7gv6c
Source0:	nagios-nuvola-%{version}.tar.gz
# Source0-md5:	3efea279c54ea2d11f259e55b0b7ba8f
URL:		http://tinyurl.com/a946b
BuildRequires:	tar >= 1:1.15.1
Obsoletes:	nagios-theme
Provides:	nagios-theme
Requires:	nagios-cgi >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_nagiosdir	/usr/share/nagios

%description
Complete Nagios Style (Menu,Icons,Stylesheets,Images) for Nagios 2.0.

Style had been updated to version 1.0 with the free DTree menu.

This is a complete image pack, menu and stylesheets for Nagios 2.0.
Icons are from the Nuvola KDE theme (http://www.icon-king.com/)

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_nagiosdir}
cp -a html/* $RPM_BUILD_ROOT%{_nagiosdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_nagiosdir}/*
