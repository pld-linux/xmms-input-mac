Summary:	This is an input plugin for XMMS which plays ape
Summary(pl):	Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±ca pliki ape
Name:		xmms-input-mac
Version:	0.5
Release:	0.1
License:	unknown
Group:		X11/Applications/Sound
Source0:	http://web.mit.edu/ddopson/xmms-mac/xmms-mac.tar.bz2
# NoSource0-md5:	35a668d0bcbd4939e7ae612e58f19684
BuildRequires:	sed >= 4.0
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin for XMMS can play monkey's ape audio files.

%description -l pl
Wtyczka dla XMMS umo¿liwiaj±ca odtwarzanie plików w formacie ape
(monkey's Audio).

%prep
%setup -q -c

sed -i -e 's@-O3 -shared@-shared %{rpmcflags}@' Makefile

%build
%{__make} build \
	CPPOPT="%{rpmcflags}" \
	COMPILER="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install libmacinput.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/*.so
