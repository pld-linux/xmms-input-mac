Summary:	Input plugin for XMMS which plays ape
Summary(pl):	Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±ca pliki ape
Name:		xmms-input-mac
Version:	0.3.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/mac-port/xmms-mac-%{version}.tar.gz
# Source0-md5:	b7a0b8225bdf519d4f2f9537da925c3d
URL:		http://sourceforge.net/projects/mac-port/
BuildRequires:	sed >= 4.0
BuildRequires:	mac-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for XMMS playing Monkey's Audio Codec (ape) files.

%description -l pl
Wtyczka dla XMMS umo¿liwiaj±ca odtwarzanie plików w formacie ape
(Monkey's Audio Codec).

%prep
%setup -q -n xmms-mac-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
