Summary:	A JSON implementation in C
Name:		json-c
Version:	0.12
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	https://s3.amazonaws.com/%{name}_releases/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3ca4bbb881dfc4017e8021b5e0a8c491
URL:		http://oss.metaparadigm.com/json-c/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags   -Wno-error

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
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libjson-c.so.2
%attr(755,root,root) %{_libdir}/libjson-c.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjson-c.so
%{_includedir}/json-c
%{_pkgconfigdir}/json-c.pc

