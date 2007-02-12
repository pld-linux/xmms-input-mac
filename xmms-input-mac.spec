Summary:	Input plugin for XMMS which plays ape
Summary(pl.UTF-8):   Wtyczka wejściowa dla XMMS-a odtwarzająca pliki ape
Name:		xmms-input-mac
Version:	0.3.1
Release:	1
Epoch:		1
# license conflict with mac
License:	GPL (for personal and educational use; non-distributable in binary form)
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/mac-port/xmms-mac-%{version}.tar.gz
# Source0-md5:	7a4be5e3433c68f155f5b2913e4f21ba
URL:		http://sourceforge.net/projects/mac-port/
BuildRequires:	sed >= 4.0
BuildRequires:	mac-devel
BuildRequires:	xmms-devel
# because of mac
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for XMMS playing Monkey's Audio Codec (ape) files.

%description -l pl.UTF-8
Wtyczka dla XMMS umożliwiająca odtwarzanie plików w formacie ape
(Monkey's Audio Codec).

%prep
%setup -q -n xmms-mac-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
