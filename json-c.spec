%define		rdate	20120530

Summary:	A JSON implementation in C
Name:		json-c
Version:	0.10
Release:	1
License:	LGPL v2
Group:		Development/Libraries
#Source0:	http://oss.metaparadigm.com/json-c/%{name}-%{version}.tar.gz
Source0:	https://github.com/json-c/json-c/archive/%{name}-%{version}-%{rdate}.tar.gz
# Source0-md5:	756c1ee48d573559a1e3662e0805325f
URL:		http://oss.metaparadigm.com/json-c/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package devel
Summary:	Header files for the json-c library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the json-c library.

%prep
%setup -qn %{name}-%{name}-%{version}-%{rdate}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libjson.so.?
%attr(755,root,root) %{_libdir}/libjson.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/json
%attr(755,root,root) %{_libdir}/libjson.so
%{_libdir}/libjson.la
%{_pkgconfigdir}/json.pc

