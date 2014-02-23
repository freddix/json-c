%define		rdate	20130402

Summary:	A JSON implementation in C
Name:		json-c
Version:	0.11
Release:	2
License:	LGPL v2
Group:		Development/Libraries
#Source0:	http://oss.metaparadigm.com/json-c/%{name}-%{version}.tar.gz
Source0:	https://github.com/json-c/json-c/archive/%{name}-%{version}-%{rdate}.tar.gz
# Source0-md5:	7013b2471a507942eb8ed72a5d872d16
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
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# link with libjson-c directly (stub libjson won't work with
# --no-copy-dt-needed-entries
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libjson-c.so.*.*.*) \
    $RPM_BUILD_ROOT%{_libdir}/libjson.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%pretrans devel
# transition from 0.11-1
[ ! -L %{_includedir}/json-c ] || rm -f %{_includedir}/json-c
# transition from <= 0.10 and 0.11-1
if [ -d %{_includedir}/json -a ! -d %{_includedir}/json-c ]; then
        mv -f %{_includedir}/json %{_includedir}/json-c
        ln -sf json-c %{_includedir}/json
fi

%files
%defattr(644,root,root,755)
%doc README INSTALL AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libjson-c.so.2
%attr(755,root,root) %ghost %{_libdir}/libjson.so.0
%attr(755,root,root) %{_libdir}/libjson-c.so.*.*.*
%attr(755,root,root) %{_libdir}/libjson.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjson-c.so
%attr(755,root,root) %{_libdir}/libjson.so
%{_includedir}/json
%{_includedir}/json-c
%{_pkgconfigdir}/json-c.pc
%{_pkgconfigdir}/json.pc

